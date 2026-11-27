#!/usr/bin/env python3
"""War dice against the capybara, played through issues.

A visitor opens an issue titled "war|roll" from the link in the README, and
.github/workflows/war-dice.yml runs this script. It rolls every open roll
issue, oldest first (a burst of clicks can cancel queued runs, so each run
drains the whole queue), saves the score in game/state.json, redraws
assets/dice-*.svg and the scoreboard in both READMEs, pushes, and only then
answers and closes each issue. Visitor input is only ever read as data here,
never passed to a shell.
"""
import datetime as dt
import json
import os
import re
import secrets
import subprocess
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build as B  # noqa: E402

API = 'https://api.github.com'
REPO = os.environ.get('GITHUB_REPOSITORY', 'tavmata/tavmata')
TOKEN = os.environ.get('GITHUB_TOKEN', '')
STATE = B.ROOT / 'game' / 'state.json'
COOLDOWN = dt.timedelta(minutes=10)
LOGIN_RE = re.compile(r'[A-Za-z0-9][A-Za-z0-9-]{0,38}')


def api(method, path, body=None):
    req = urllib.request.Request(
        API + path, method=method, data=None if body is None else json.dumps(body).encode(),
        headers={'Authorization': f'Bearer {TOKEN}', 'Accept': 'application/vnd.github+json',
                 'X-GitHub-Api-Version': '2022-11-28', 'User-Agent': 'war-dice'})
    with urllib.request.urlopen(req, timeout=30) as r:
        text = r.read().decode('utf-8')
    return json.loads(text) if text else None


def open_rolls():
    issues = api('GET', f'/repos/{REPO}/issues?state=open&sort=created&direction=asc&per_page=50')
    return [i for i in issues if 'pull_request' not in i and i['title'].strip().lower() == 'war|roll']


verdict = B.verdict


def git(*args):
    subprocess.run(['git', *args], check=True)


def push(message):
    git('config', 'user.name', 'github-actions[bot]')
    git('config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com')
    git('add', 'game/state.json', 'assets/dice-en.svg', 'assets/dice-pt.svg', 'README.md', 'README.pt-BR.md')
    git('commit', '-q', '-m', message)
    for _ in range(4):
        if subprocess.run(['git', 'push', '-q']).returncode == 0:
            return
        git('pull', '-q', '--rebase')
    sys.exit('push failed; the issues stay open for the next run')


def main():
    todo = open_rolls()
    if not todo:
        print('no open rolls')
        return
    state = json.loads(STATE.read_text(encoding='utf-8'))
    now = dt.datetime.now(dt.timezone.utc)
    replies, rolled = [], []
    for issue in todo:
        number, user = issue['number'], issue['user']
        login = user.get('login', '')
        if user.get('type') != 'User' or not LOGIN_RE.fullmatch(login):
            replies.append((number, 'Only people can roll against the capybara.\n\nSó gente pode rolar contra a capivara.'))
            continue
        prev = next((r for r in state['rolls'] if r['login'].lower() == login.lower()), None)
        if prev and now - dt.datetime.fromisoformat(prev['at']) < COOLDOWN:
            replies.append((number, 'One roll every 10 minutes per player. Try again in a little while.\n\n'
                                    'Uma rolagem a cada 10 minutos por jogador. Tente de novo daqui a pouco.'))
            continue
        red, yellow = secrets.randbelow(6) + 1, secrets.randbelow(6) + 1
        state['visitors' if red > yellow else 'capybara'] += 1
        state['total'] = state.get('total', 0) + 1
        state['rolls'].insert(0, {'n': state['total'], 'login': login, 'red': red, 'yellow': yellow,
                                  'at': now.isoformat(timespec='seconds'), 'issue': number})
        del state['rolls'][20:]
        v, c = state['visitors'], state['capybara']
        replies.append((number,
                        f'Attack {red} × {yellow} defence: {verdict(red, yellow, "en")}. '
                        f'Score: visitors {v}, capybara {c}. Your roll is on https://github.com/tavmata now.\n\n'
                        f'Ataque {red} × {yellow} defesa: {verdict(red, yellow, "pt")}. '
                        f'Placar: visitantes {v}, capivara {c}. A sua rolagem já está no perfil.'))
        rolled.append(f'{login} {red}×{yellow}')

    if rolled:
        STATE.write_text(json.dumps(state, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
        for lang, readme in (('en', 'README.md'), ('pt', 'README.pt-BR.md')):
            (B.ASSETS / f'dice-{lang}.svg').write_text(B.dice_card(lang, state), encoding='utf-8')
            B.fill(readme, 'dice', B.dice_board(lang, state))
            path = B.ROOT / readme
            text = re.sub(rf'(assets/dice-{lang}\.svg)\?v=\d+', rf'\g<1>?v={state["total"]}',
                          path.read_text(encoding='utf-8'))
            path.write_text(text, encoding='utf-8')
        push('War dice: ' + ', '.join(rolled))
    for number, body in replies:
        api('POST', f'/repos/{REPO}/issues/{number}/comments', {'body': body})
        api('PATCH', f'/repos/{REPO}/issues/{number}', {'state': 'closed', 'state_reason': 'completed'})
    print('rolled:', rolled or 'none', '| answered:', len(replies))


if __name__ == '__main__':
    main()
