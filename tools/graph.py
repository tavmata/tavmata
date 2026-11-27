#!/usr/bin/env python3
"""The live card: a year of GitHub contributions drawn as a field of pinhões,
and the capybara from the kich.dev.br living room eating them day by day.

    python3 tools/graph.py <output dir>

Runs every day in .github/workflows/capybara.yml, which publishes the two
SVGs (capybara-en.svg, capybara-pt.svg) to the `output` branch. Reads the
public contribution calendar: GraphQL with GITHUB_TOKEN when there is one,
and the calendar page itself otherwise (or when it reports more).
"""
import datetime as dt
import json
import os
import re
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build as B  # noqa: E402  (pixel font, palette, svg helpers)

LOGIN = 'tavmata'
LEVELS = {'NONE': 0, 'FIRST_QUARTILE': 1, 'SECOND_QUARTILE': 2, 'THIRD_QUARTILE': 3, 'FOURTH_QUARTILE': 4}
MONTHS = {'en': 'JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC'.split(),
          'pt': 'JAN FEV MAR ABR MAI JUN JUL AGO SET OUT NOV DEZ'.split()}
TEXT = {
    'en': {'live': 'LIVE', 'upd': 'UPDATED {d}', 'total': '{n} CONTRIBUTIONS IN THE LAST YEAR',
           'streak': 'CURRENT STREAK: {c} · LONGEST: {l}', 'days': lambda n: f'{n} DAY' if n == 1 else f'{n} DAYS',
           'less': 'LESS', 'more': 'MORE',
           'aria': 'A year of GitHub contributions drawn as pinhões, with a pixel capybara walking across and eating them'},
    'pt': {'live': 'AO VIVO', 'upd': 'ATUALIZADO EM {d}', 'total': '{n} CONTRIBUIÇÕES NO ÚLTIMO ANO',
           'streak': 'SEQUÊNCIA ATUAL: {c} · RECORDE: {l}', 'days': lambda n: f'{n} DIA' if n == 1 else f'{n} DIAS',
           'less': 'MENOS', 'more': 'MAIS',
           'aria': 'Um ano de contribuições no GitHub desenhado como pinhões, com uma capivara em pixel atravessando e comendo'},
}


def _get(url, headers, data=None):
    req = urllib.request.Request(url, data=data, headers={'User-Agent': 'tavmata-profile-card', **headers})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode('utf-8')


def from_graphql(token):
    q = ('{user(login:"%s"){contributionsCollection{contributionCalendar{weeks{contributionDays'
         '{date contributionCount contributionLevel}}}}}}' % LOGIN)
    d = json.loads(_get('https://api.github.com/graphql', {'Authorization': f'bearer {token}'},
                        json.dumps({'query': q}).encode()))
    weeks = d['data']['user']['contributionsCollection']['contributionCalendar']['weeks']
    return [(x['date'], x['contributionCount'], LEVELS[x['contributionLevel']]) for w in weeks for x in w['contributionDays']]


def from_page():
    h = _get(f'https://github.com/users/{LOGIN}/contributions', {})
    tips = {m.group(1): m.group(2) for m in re.finditer(r'<tool-tip[^>]*\bfor="([^"]+)"[^>]*>([^<]*)</tool-tip>', h)}
    days = []
    for m in re.finditer(r'<td\b[^>]*ContributionCalendar-day[^>]*>', h):
        tag = m.group(0)
        date, level, ident = (re.search(rf'{k}="([^"]+)"', tag) for k in ('data-date', 'data-level', 'id'))
        if not (date and level and ident):
            continue
        n = re.match(r'([\d,]+) contribution', tips.get(ident.group(1), ''))
        days.append((date.group(1), int(n.group(1).replace(',', '')) if n else 0, int(level.group(1))))
    return sorted(days)


def calendar():
    found = []
    token = os.environ.get('GITHUB_TOKEN')
    if token:
        try:
            found.append(from_graphql(token))
        except Exception as e:  # keep going with the page
            print('graphql failed:', e)
    try:
        found.append(from_page())
    except Exception as e:
        print('page failed:', e)
    found = [f for f in found if f]
    if not found:
        sys.exit('no contribution data')
    return max(found, key=lambda days: sum(n for _, n, _ in days))


def streaks(days):
    counts = [n for _, n, _ in days]
    longest = run = 0
    for n in counts:
        run = run + 1 if n else 0
        longest = max(longest, run)
    i = len(counts) - 1
    if i >= 0 and counts[i] == 0:  # today may still be empty
        i -= 1
    current = 0
    while i >= 0 and counts[i]:
        current += 1
        i -= 1
    return current, longest


def card(days, lang, today):
    T = TEXT[lang]
    pt = lang == 'pt'
    pal = B.ROOM['pal']
    W, H = 900, 272
    cell, x0, y0 = 15, 53, 132
    first = dt.date.fromisoformat(days[0][0])
    lead = (first.weekday() + 1) % 7  # GitHub weeks start on Sunday
    pos = []
    for i, (d, n, lv) in enumerate(days):
        k = i + lead
        pos.append((x0 + (k // 7) * cell + cell // 2, y0 + (k % 7) * cell + cell // 2))
    total = sum(n for _, n, _ in days)
    cur, best = streaks(days)
    fmt = (lambda v: f'{v:,}'.replace(',', '.')) if pt else (lambda v: f'{v:,}')

    b = [f'<rect width="{W}" height="{H}" rx="14" fill="#0A171C"/>']
    # header
    dot = [(x, y) for y in range(4) for x in range(4) if (x, y) not in ((0, 0), (3, 0), (0, 3), (3, 3))]
    b.append(f'<g class="dot">{B.pix(dot, "#E8483C", 24, 25, 3)}</g>')
    b.append(B.ptext(T['live'], 44, 24, 2, '#E8483C'))
    stamp = today.strftime('%d/%m/%Y') if pt else today.isoformat()
    b.append(B.ptext(T['upd'].format(d=stamp), W - 24, 24, 2, '#6E767C', anchor='end'))
    b.append(B.ptext(T['total'].format(n=fmt(total)), 24, 56, 3, '#F2E6B6', shadow='#4A2412'))
    b.append(B.ptext(T['streak'].format(c=T['days'](cur), l=T['days'](best)), 24, 92, 2, '#A3ACB3'))
    # month labels where a month starts
    last_col = -9
    for i, (d, _, _) in enumerate(days):
        day = dt.date.fromisoformat(d)
        col = (i + lead) // 7
        if day.day == 1 and col - last_col >= 3 and col < 51:
            b.append(B.ptext(MONTHS[lang][day.month - 1], x0 + col * cell, 114, 2, '#46B154'))
            last_col = col
    # pinhão symbol and the field
    pin = []
    for r, line in enumerate(B.ROOM['pinhao']):
        for c, ch in enumerate(line):
            if ch != '.':
                pin.append(f'<rect x="{c * 2 - 3}" y="{r * 2 - 5}" width="2" height="2" fill="{pal[ch]}"/>')
    capy = []
    for y, line in enumerate(B.ROOM['capybara']):
        for x, ch in enumerate(line):
            if ch != '.':
                capy.append(((x - 28, y - 6), pal[ch]))
    capy_d = {}
    for (x, y), col in capy:  # drawn at 2x, the mouth sits on the point it walks to
        capy_d.setdefault(col, []).append(f'M{x * 2} {y * 2}h2v2h-2z')
    capy_paths = ''.join(f'<path fill="{c}" d="{" ".join(v)}"/>' for c, v in capy_d.items())
    defs = f'<defs><g id="pin">{"".join(pin)}</g><g id="capy">{capy_paths}</g></defs>'
    empty = ''.join(f'M{x - 1} {y - 1}h3v3h-3z' for (x, y), (_, _, lv) in zip(pos, days) if lv == 0)
    b.append(f'<path fill="#17404C" d="{empty}"/>')

    # the walk: every day with contributions, in order, at a steady pace
    eat = [(p, i) for i, (p, (_, _, lv)) in enumerate(zip(pos, days)) if lv > 0]
    pts = [(eat[0][0][0] - 70, eat[0][0][1])] + [p for p, _ in eat] + [(W + 60, eat[-1][0][1])] if eat else []
    seg = [((bx - ax) ** 2 + (by - ay) ** 2) ** .5 for (ax, ay), (bx, by) in zip(pts, pts[1:])]
    speed = max(130.0, sum(seg) / 26)
    times = [0.0]
    for s in seg:
        times.append(times[-1] + max(s / speed, 0.11))
    period = (times[-1] if times else 0) + 2.0
    opacity = {1: .4, 2: .62, 3: .82, 4: 1}
    for k, ((x, y), i) in enumerate(eat):
        lv = days[i][2]
        b.append(f'<g opacity="{opacity[lv]}"><use href="#pin" x="{x}" y="{y}" class="p" '
                 f'style="animation-delay:{times[k + 1]:.2f}s"/></g>')
    frames = []
    direction = 1
    for j, ((x, y), t) in enumerate(zip(pts, times)):
        nxt = pts[j + 1][0] - x if j + 1 < len(pts) else 0
        new = direction if abs(nxt) < 1 else (1 if nxt > 0 else -1)
        pct = 100 * t / period
        frames.append(f'{pct:.3f}%{{transform:translate({x}px,{y}px) scale({direction},1)}}')
        if new != direction:
            frames.append(f'{pct + .001:.3f}%{{transform:translate({x}px,{y}px) scale({new},1)}}')
            direction = new
    if pts:
        frames.append(f'100%{{transform:translate({pts[-1][0]}px,{pts[-1][1]}px) scale({direction},1)}}')
        b.append(f'<g class="capy"><use href="#capy"/></g>')
    # legend
    lx = W - 30 - B.text_width(T['more'], 2)
    b.append(B.ptext(T['more'], W - 24, 252, 2, '#6E767C', anchor='end'))
    for lv in (4, 3, 2, 1):
        lx -= 16
        b.append(f'<g opacity="{opacity[lv]}"><use href="#pin" x="{lx + 6}" y="{258}"/></g>')
    lx -= 16
    b.append(f'<path fill="#17404C" d="M{lx + 5} {257}h3v3h-3z"/>')
    b.append(B.ptext(T['less'], lx - 6, 252, 2, '#6E767C', anchor='end'))

    gone = 100 * 4.0 / period  # an eaten pinhão grows back four seconds later
    style = (f'.p{{transform-box:fill-box;transform-origin:center;animation:eat {period:.2f}s infinite}}'
             f'@keyframes eat{{0%{{opacity:0;transform:scale(.2)}}{gone:.2f}%{{opacity:0;transform:scale(.2)}}'
             f'{gone + 1.5:.2f}%{{opacity:1;transform:scale(1)}}100%{{opacity:1;transform:scale(1)}}}}'
             f'.capy{{transform-origin:0 0;animation:walk {period:.2f}s linear infinite}}'
             f'@keyframes walk{{{"".join(frames)}}}'
             '.dot{animation:blink 1.6s step-end infinite}@keyframes blink{50%{opacity:0}}'
             '@media (prefers-reduced-motion:reduce){.p,.dot{animation:none}.capy{display:none}}')
    return B.svg(W, H, defs + ''.join(b), T['aria'], style)


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else 'dist'
    os.makedirs(out, exist_ok=True)
    days = calendar()
    today = dt.datetime.now(dt.timezone(dt.timedelta(hours=-3))).date()  # Florianópolis
    for lang in ('en', 'pt'):
        path = os.path.join(out, f'capybara-{lang}.svg')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(card(days, lang, today))
        print(path, sum(n for _, n, _ in days), 'contributions,', len(days), 'days')


if __name__ == '__main__':
    main()
