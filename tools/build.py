#!/usr/bin/env python3
"""Builds the animated SVGs and the map data used by the profile README.

    python tools/build.py

Everything is drawn in code, the same way kich.dev.br is: the header is the
site's 72 x 72 pixel room (tools/room.json, exported from the site), and each
card follows the style of one TV channel of the site. The numbers come from
the site (commits per hour) and from the SISMIGRA dashboard
(github.com/tavmata/painel-sul-sul-sismigra).

Outputs go to assets/: header, clock, passport, blueprint, sheet and end-card
SVGs in English and Portuguese. It also refreshes the map and the table
between the <!-- map --> and <!-- table --> markers in both READMEs.
"""
import json
import math
import random
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / 'assets'
ROOM = json.loads((ROOT / 'tools' / 'room.json').read_text(encoding='utf-8'))

# ---------------------------------------------------------------- pixel font
# 5x7 capitals, variable width for punctuation. '#' is ink.
F = {
    'A': ['.###.', '#...#', '#...#', '#####', '#...#', '#...#', '#...#'],
    'B': ['####.', '#...#', '#...#', '####.', '#...#', '#...#', '####.'],
    'C': ['.###.', '#...#', '#....', '#....', '#....', '#...#', '.###.'],
    'D': ['####.', '#...#', '#...#', '#...#', '#...#', '#...#', '####.'],
    'E': ['#####', '#....', '#....', '####.', '#....', '#....', '#####'],
    'F': ['#####', '#....', '#....', '####.', '#....', '#....', '#....'],
    'G': ['.###.', '#...#', '#....', '#.###', '#...#', '#...#', '.####'],
    'H': ['#...#', '#...#', '#...#', '#####', '#...#', '#...#', '#...#'],
    'I': ['###', '.#.', '.#.', '.#.', '.#.', '.#.', '###'],
    'J': ['..###', '...#.', '...#.', '...#.', '...#.', '#..#.', '.##..'],
    'K': ['#...#', '#..#.', '#.#..', '##...', '#.#..', '#..#.', '#...#'],
    'L': ['#....', '#....', '#....', '#....', '#....', '#....', '#####'],
    'M': ['#...#', '##.##', '#.#.#', '#.#.#', '#...#', '#...#', '#...#'],
    'N': ['#...#', '#...#', '##..#', '#.#.#', '#..##', '#...#', '#...#'],
    'O': ['.###.', '#...#', '#...#', '#...#', '#...#', '#...#', '.###.'],
    'P': ['####.', '#...#', '#...#', '####.', '#....', '#....', '#....'],
    'Q': ['.###.', '#...#', '#...#', '#...#', '#.#.#', '#..#.', '.##.#'],
    'R': ['####.', '#...#', '#...#', '####.', '#.#..', '#..#.', '#...#'],
    'S': ['.####', '#....', '#....', '.###.', '....#', '....#', '####.'],
    'T': ['#####', '..#..', '..#..', '..#..', '..#..', '..#..', '..#..'],
    'U': ['#...#', '#...#', '#...#', '#...#', '#...#', '#...#', '.###.'],
    'V': ['#...#', '#...#', '#...#', '#...#', '#...#', '.#.#.', '..#..'],
    'W': ['#...#', '#...#', '#...#', '#.#.#', '#.#.#', '#.#.#', '.#.#.'],
    'X': ['#...#', '#...#', '.#.#.', '..#..', '.#.#.', '#...#', '#...#'],
    'Y': ['#...#', '#...#', '.#.#.', '..#..', '..#..', '..#..', '..#..'],
    'Z': ['#####', '....#', '...#.', '..#..', '.#...', '#....', '#####'],
    '0': ['.###.', '#...#', '#..##', '#.#.#', '##..#', '#...#', '.###.'],
    '1': ['..#..', '.##..', '..#..', '..#..', '..#..', '..#..', '.###.'],
    '2': ['.###.', '#...#', '....#', '...#.', '..#..', '.#...', '#####'],
    '3': ['####.', '....#', '....#', '.###.', '....#', '....#', '####.'],
    '4': ['...#.', '..##.', '.#.#.', '#..#.', '#####', '...#.', '...#.'],
    '5': ['#####', '#....', '####.', '....#', '....#', '#...#', '.###.'],
    '6': ['.###.', '#....', '#....', '####.', '#...#', '#...#', '.###.'],
    '7': ['#####', '....#', '...#.', '..#..', '.#...', '.#...', '.#...'],
    '8': ['.###.', '#...#', '#...#', '.###.', '#...#', '#...#', '.###.'],
    '9': ['.###.', '#...#', '#...#', '.####', '....#', '....#', '.###.'],
    ' ': ['..', '..', '..', '..', '..', '..', '..'],
    '.': ['.', '.', '.', '.', '.', '.', '#'],
    ',': ['..', '..', '..', '..', '.#', '.#', '#.'],
    ':': ['.', '.', '#', '.', '.', '#', '.'],
    '·': ['.', '.', '.', '#', '.', '.', '.'],
    '-': ['...', '...', '...', '###', '...', '...', '...'],
    '–': ['....', '....', '....', '####', '....', '....', '....'],
    "'": ['#', '#', '.', '.', '.', '.', '.'],
    '!': ['#', '#', '#', '#', '#', '.', '#'],
    '(': ['.#', '#.', '#.', '#.', '#.', '#.', '.#'],
    ')': ['#.', '.#', '.#', '.#', '.#', '.#', '#.'],
    '/': ['....#', '...#.', '...#.', '..#..', '.#...', '.#...', '#....'],
    '+': ['.....', '..#..', '..#..', '#####', '..#..', '..#..', '.....'],
    '%': ['##..#', '##.#.', '...#.', '..#..', '.#...', '.#.##', '#..##'],
    '>': ['#...', '.#..', '..#.', '...#', '..#.', '.#..', '#...'],
    '<': ['...#', '..#.', '.#..', '#...', '.#..', '..#.', '...#'],
    '▶': ['#...', '##..', '###.', '####', '###.', '##..', '#...'],
    '×': ['.....', '.....', '#...#', '.#.#.', '..#..', '.#.#.', '#...#'],
    '#': ['.#.#.', '.#.#.', '#####', '.#.#.', '#####', '.#.#.', '.#.#.'],
    '@': ['.###.', '#...#', '#.###', '#.#.#', '#.###', '#....', '.####'],
}
ACCENT = {
    'acute': ['...#.', '..#..'], 'grave': ['.#...', '..#..'],
    'circ': ['..#..', '.#.#.'], 'tilde': ['.##.#', '#..#.'],
}
ACCENTED = {
    'Á': ('A', 'acute'), 'À': ('A', 'grave'), 'Â': ('A', 'circ'), 'Ã': ('A', 'tilde'),
    'É': ('E', 'acute'), 'Ê': ('E', 'circ'), 'Í': ('I', 'acute'), 'Ó': ('O', 'acute'),
    'Ô': ('O', 'circ'), 'Õ': ('O', 'tilde'), 'Ú': ('U', 'acute'),
}


def glyph(ch):
    """Returns (rows, top) where top is the row offset of rows[0] (accents sit at -2)."""
    if ch in F:
        return F[ch], 0
    if ch == 'Ç':
        return F['C'] + ['..#..', '.##..'], 0
    if ch in ACCENTED:
        base, acc = ACCENTED[ch]
        rows = F[base]
        mark = ACCENT[acc]
        if len(rows[0]) != 5:  # narrow I: centre the mark
            mark = [r[1:4] for r in mark]
        return mark + rows, -2
    raise KeyError(f'no glyph for {ch!r}')


def text_width(s, scale):
    w = 0
    for ch in s:
        rows, _ = glyph(ch)
        w += (len(rows[0]) + 1) * scale
    return w - scale if s else 0


def text_runs(s, x, y, scale):
    """Pixel runs (x, y, w) for a string whose cap height starts at y."""
    runs = []
    cx = x
    for ch in s:
        rows, top = glyph(ch)
        for r, line in enumerate(rows):
            c = 0
            while c < len(line):
                if line[c] != '#':
                    c += 1
                    continue
                c2 = c
                while c2 + 1 < len(line) and line[c2 + 1] == '#':
                    c2 += 1
                runs.append((cx + c * scale, y + (top + r) * scale, (c2 - c + 1) * scale))
                c = c2 + 1
        cx += (len(rows[0]) + 1) * scale
    return runs


def runs_d(runs, h):
    return ''.join(f'M{x} {y}h{w}v{h}h-{w}z' for x, y, w in runs)


def ptext(s, x, y, scale, fill, shadow=None, anchor='start', cls=''):
    """Pixel text as one path (plus an optional 1-pixel drop shadow)."""
    if anchor == 'end':
        x -= text_width(s, scale)
    elif anchor == 'middle':
        x -= text_width(s, scale) // 2
    c = f' class="{cls}"' if cls else ''
    out = ''
    if shadow:
        out += f'<path{c} fill="{shadow}" d="{runs_d(text_runs(s, x + scale, y + scale, scale), scale)}"/>'
    out += f'<path{c} fill="{fill}" d="{runs_d(text_runs(s, x, y, scale), scale)}"/>'
    return out


def pix(points, color, ox, oy, p):
    d = ''.join(f'M{ox + x * p} {oy + y * p}h{p}v{p}h-{p}z' for x, y in points)
    return f'<path fill="{color}" d="{d}"/>'


def svg(w, h, body, title, style=''):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'role="img" aria-label="{escape(title)}"><title>{escape(title)}</title>'
            f'<style>{style}</style>{body}</svg>\n')


def write(name, text):
    (ASSETS / name).write_text(text, encoding='utf-8')
    print(f'{name:28s} {len(text.encode("utf-8")) / 1024:7.1f} KB')


# ---------------------------------------------------------------- header
CHANNELS = [  # number, English, Portuguese, screen background, screen ink
    ('01', 'LIVING ROOM', 'SALA', None, '#46B154'),
    ('02', 'KAPI ONLINE', 'KAPI ONLINE', '#1A120D', '#E08A4A'),
    ('04', 'RESEARCH', 'PESQUISA', '#F4F0E2', '#2D5DB8'),
    ('05', 'PASSPORT', 'PASSAPORTE', '#1E2C55', '#D4AF4F'),
    ('06', 'DASHBOARD', 'PAINEL', '#FF5AA5', '#1F5FD1'),
    ('08', 'ARCADE', 'FLIPERAMA', '#FFFFFF', '#111111'),
    ('09', 'CV', 'FICHA', '#2338A0', '#FFFFFF'),
    ('10', 'CORDEL', 'CORDEL', '#EDE3C8', '#161616'),
    ('11', 'THE END', 'FIM', None, '#F4F6F6'),
]
DIG = {
    '0': ['###', '#.#', '#.#', '#.#', '###'], '1': ['.#.', '##.', '.#.', '.#.', '###'],
    '2': ['###', '..#', '###', '#..', '###'], '3': ['###', '..#', '.##', '..#', '###'],
    '4': ['#.#', '#.#', '###', '..#', '..#'], '5': ['###', '#..', '###', '..#', '###'],
    '6': ['###', '#..', '###', '#.#', '###'], '7': ['###', '..#', '..#', '.#.', '.#.'],
    '8': ['###', '#.#', '###', '#.#', '###'], '9': ['###', '#.#', '###', '..#', '###'],
}
BARS = ['#C0C0C0', '#C0C000', '#00C0C0', '#00C000', '#C000C0', '#C00000', '#0000C0']
HEADER_TEXT = {
    'en': {'place': 'FLORIANÓPOLIS · BRAZIL', 'l1': 'INTERNATIONAL RELATIONS · UFSC',
           'l2': 'MIGRATION RESEARCH · GAMES · DATA', 'now': 'NOW SHOWING',
           'title': 'Otávio Kich Mata: a pixel living room where the TV flips through the channels of kich.dev.br'},
    'pt': {'place': 'FLORIANÓPOLIS · BRASIL', 'l1': 'RELAÇÕES INTERNACIONAIS · UFSC',
           'l2': 'MIGRAÇÃO · JOGOS · DADOS', 'now': 'NO AR AGORA',
           'title': 'Otávio Kich Mata: uma sala em pixel onde a TV troca entre os canais do kich.dev.br'},
}


def header(lang):
    T = HEADER_TEXT[lang]
    W, H, P, OX, OY = 1000, 304, 4, 16, 8
    room = ROOM['room']
    pal = ROOM['pal']
    body = [f'<rect width="{W}" height="{H}" rx="14" fill="#0A171C"/>']

    # the room, merged into one path per colour
    runs = {}
    for y, row in enumerate(room):
        x = 0
        while x < 72:
            c = row[x]
            if c == '.':
                x += 1
                continue
            x2 = x
            while x2 + 1 < 72 and row[x2 + 1] == c:
                x2 += 1
            runs.setdefault(pal[c], []).append((OX + x * P, OY + y * P, (x2 - x + 1) * P))
            x = x2 + 1
    body.append('<g>' + ''.join(f'<path fill="{c}" d="{runs_d(r, P)}"/>' for c, r in runs.items()) + '</g>')

    # TV screen: every pixel of the 13 x 12 window that is not bezel
    sx, sy, sw, sh = 27, 18, 13, 12
    mask = [(x, y) for y in range(sy, sy + sh) for x in range(sx, sx + sw) if room[y][x] != 'K']
    rnd = random.Random(7)
    greys = ['#0B0F16', '#2A3A40', '#6E767C', '#A3ACB3', '#D9DDDF', '#F4F6F6']
    for k in range(2):
        noise = {}
        for p in mask:
            noise.setdefault(rnd.choice(greys), []).append(p)
        body.append(f'<g class="noise n{k}">' + ''.join(pix(v, c, OX, OY, P) for c, v in noise.items()) + '</g>')

    # channel states: screen card + "now showing" chip, shown one at a time
    chip_x, chip_y, chip_h = 340, 238, 44
    names = [c[1] if lang == 'en' else c[2] for c in CHANNELS]
    chip_w = max(text_width(f'▶ CH {c[0]} · {n}', 3) for c, n in zip(CHANNELS, names)) + 32
    for k, ((num, _en, _pt, bg, ink), name) in enumerate(zip(CHANNELS, names)):
        g = [f'<g class="st s{k}" style="animation-delay:{k * 3}s">']
        if num == '11':  # end of broadcast: colour bars
            for i, c in enumerate(BARS):
                cols = [(x, y) for (x, y) in mask if (x - sx) * 7 // sw == i]
                g.append(pix(cols, c, OX, OY, P))
        elif bg:
            g.append(pix(mask, bg, OX, OY, P))
            digs = []
            for i, d in enumerate(num):
                for r, line in enumerate(DIG[d]):
                    for c, ch in enumerate(line):
                        if ch == '#':
                            digs.append((sx + 3 + i * 4 + c, sy + 3 + r))
            g.append(pix(digs, ink, OX, OY, P))
        label = f'▶ CH {num} · {name}'
        cbg = bg or '#14303A'
        cink = ink if num != '11' else '#F4F6F6'
        if num == '11':
            cbg = '#111111'
        g.append(f'<rect x="{chip_x}" y="{chip_y}" width="{chip_w}" height="{chip_h}" fill="{cbg}" '
                 f'stroke="#F4F6F6" stroke-opacity=".18" stroke-width="2"/>')
        g.append(ptext(label, chip_x + 16, chip_y + 12, 3, cink))
        g.append('</g>')
        body.append(''.join(g))

    # blinking eyes, twinkling stars, the hidden pinhão (only on the last channel)
    body.append(f'<g class="blink">{pix([(22, 55), (23, 55)], pal["d"], OX, OY, P)}</g>')
    body.append(f'<g class="blink" style="animation-delay:2.4s">{pix([(53, 33), (54, 33)], pal["x"], OX, OY, P)}</g>')
    for i, (x, y) in enumerate([(6, 7), (10, 9), (4, 11), (18, 11)]):
        body.append(f'<g class="tw" style="animation-delay:{i * 1.1:.1f}s">{pix([(x, y)], pal["j"], OX, OY, P)}</g>')
    pin = []
    for r, line in enumerate(ROOM['pinhao']):
        for c, ch in enumerate(line):
            if ch != '.':
                pin.append(((66 + c, 52 + r), pal[ch]))
    pin_g = ''.join(pix([p], col, OX, OY, P) for p, col in pin)
    body.append(f'<g class="st pin" style="animation-delay:{(len(CHANNELS) - 1) * 3}s">{pin_g}</g>')

    # bunting across the top, like the room's festa junina flags
    flag_cols = ['#E8483C', '#EDC04E', '#7FA6E8', '#C9713F', '#B48CD8', '#46B154']
    xs = list(range(330, 1000, 44))
    pts = []
    for i, x in enumerate(xs):
        t = (x - 300) / 700
        y = 6 + 14 * math.sin(math.pi * t)
        pts.append((x, y))
    body.append('<path fill="none" stroke="#2A3A40" stroke-width="2" d="M300 6 ' +
                ' '.join(f'L{x} {y:.1f}' for x, y in pts) + ' L1000 6"/>')
    for i, (x, y) in enumerate(pts):
        col = flag_cols[i % len(flag_cols)]
        y0 = round(y)
        d = f'M{x - 6} {y0}h12v12h-4v-4h-4v4h-4z'
        body.append(f'<path class="flag" style="animation-delay:{-i * 0.37:.2f}s;transform-origin:{x}px {y0}px" '
                    f'fill="{col}" d="{d}"/>')

    # text column
    X = 340
    body.append(ptext(T['place'], X, 42, 2, '#7FA6E8'))
    body.append(ptext('KICH.DEV.BR', 984, 42, 2, '#EDC04E', anchor='end'))
    body.append(ptext('OTÁVIO KICH MATA', X, 88, 5, '#F2E6B6', shadow='#8A4524'))
    body.append(ptext(T['l1'], X, 150, 3, '#D9DDDF'))
    body.append(ptext(T['l2'], X, 182, 3, '#A3ACB3'))
    body.append(ptext(T['now'], X, 220, 2, '#46B154'))

    cycle, slot = len(CHANNELS) * 3, 100 / len(CHANNELS)  # three seconds per channel
    style = (
        f'.st{{opacity:0;animation:st {cycle}s step-end infinite}}'
        f'@keyframes st{{0%{{opacity:1}}{slot:.4f}%{{opacity:0}}100%{{opacity:0}}}}'
        '.noise{opacity:0;animation:nz 3s step-end infinite}.n1{animation-delay:.12s}'
        '@keyframes nz{0%{opacity:1}4%{opacity:0}100%{opacity:0}}'
        '.blink{opacity:0;animation:bl 6s step-end infinite}'
        '@keyframes bl{0%{opacity:0}94%{opacity:1}97%{opacity:0}}'
        '.tw{opacity:0;animation:tw 4.4s step-end infinite}'
        '@keyframes tw{0%{opacity:0}55%{opacity:1}70%{opacity:0}}'
        '.flag{animation:sway 3.2s ease-in-out infinite alternate}'
        '@keyframes sway{from{transform:rotate(-7deg)}to{transform:rotate(7deg)}}'
        '@media (prefers-reduced-motion:reduce){.st,.noise,.blink,.tw,.flag{animation:none}'
        '.s0{opacity:1}}'
    )
    return svg(W, H, ''.join(body), T['title'], style)


# ---------------------------------------------------------------- passport (CH 05)
MONO = "font-family:'OCR B','OCR-B','Courier New',Courier,monospace"
SANS = "font-family:'Helvetica Neue',Helvetica,Arial,sans-serif"
PASS_TEXT = {
    'en': {'head': 'PASSPORT OF EXPERIENCES', 'ch': 'CH 05 · TRAVEL DOCUMENT',
           'fields': [('NAME', 'KICH MATA, OTÁVIO'), ('BASED IN', 'FLORIANÓPOLIS, SC'),
                      ('STUDYING', 'INTERNATIONAL RELATIONS'), ('', 'UFSC'),
                      ('LANGUAGES', 'PT · EN · ES · FR · DE · ZH')],
           'stamps': [['DPU', 'MIGRATION UNIT', 'FLORIANÓPOLIS', '12·2024 – 09·2025'],
                      ['UNV', 'UNRISD', 'REMOTE', '06 – 12·2024'],
                      ['ENAP', 'IMMIGRANT', 'RIGHTS'],
                      ['UFSCMUN', 'VII · VIII', 'ORGANIZER'],
                      ['AUGM', 'WINTER', 'SCHOOL', 'UFABC'],
                      ['BSAFE', 'UNDSS · UN', 'FIELD', 'SECURITY']],
           'aria': 'A passport page with stamps: DPU Migration Unit, UN Volunteers at UNRISD, ENAP, UFSCMUN, AUGM and BSAFE'},
    'pt': {'head': 'PASSAPORTE DE EXPERIÊNCIAS', 'ch': 'CH 05 · DOCUMENTO DE VIAGEM',
           'fields': [('NOME', 'KICH MATA, OTÁVIO'), ('BASE', 'FLORIANÓPOLIS, SC'),
                      ('CURSO', 'RELAÇÕES INTERNACIONAIS'), ('', 'UFSC'),
                      ('IDIOMAS', 'PT · EN · ES · FR · DE · ZH')],
           'stamps': [['DPU', 'NÚCLEO DE MIGRAÇÃO', 'FLORIANÓPOLIS', '12·2024 – 09·2025'],
                      ['UNV', 'UNRISD', 'REMOTO', '06 – 12·2024'],
                      ['ENAP', 'DIREITOS DOS', 'IMIGRANTES'],
                      ['UFSCMUN', 'VII · VIII', 'ORGANIZAÇÃO'],
                      ['AUGM', 'ESCOLA DE', 'INVERNO', 'UFABC'],
                      ['BSAFE', 'UNDSS · ONU', 'SEGURANÇA', 'EM CAMPO']],
           'aria': 'Uma página de passaporte com carimbos: Núcleo de Migração da DPU, Voluntários da ONU no UNRISD, ENAP, UFSCMUN, AUGM e BSAFE'},
}


def passport(lang):
    T = PASS_TEXT[lang]
    W, H = 920, 500
    b = [f'<rect width="{W}" height="{H}" rx="14" fill="#F1EBD8"/>']
    # guilloché: two families of crossing waves
    for i in range(22):
        d = []
        for x in range(0, W + 1, 8):
            y = 250 + 170 * math.sin(x / 140 + i * 0.29) * math.cos(x / 410 + i * 0.11)
            d.append(f'{"M" if x == 0 else "L"}{x} {y:.1f}')
        b.append(f'<path d="{" ".join(d)}" fill="none" stroke="#5FA394" stroke-opacity=".22" stroke-width=".9"/>')
    for i in range(14):
        d = []
        for x in range(0, W + 1, 8):
            y = 250 + 120 * math.cos(x / 95 + i * 0.45) * math.sin(x / 300 - i * 0.2)
            d.append(f'{"M" if x == 0 else "L"}{x} {y:.1f}')
        b.append(f'<path d="{" ".join(d)}" fill="none" stroke="#C7718A" stroke-opacity=".14" stroke-width=".8"/>')
    # rosette
    for i in range(36):
        b.append(f'<ellipse cx="372" cy="262" rx="96" ry="28" fill="none" stroke="#5FA394" stroke-opacity=".12" '
                 f'transform="rotate({i * 5} 372 262)"/>')
    b.append(f'<rect x="10" y="10" width="{W - 20}" height="{H - 20}" rx="8" fill="none" stroke="#24408E" stroke-opacity=".35"/>')
    b.append(f'<text x="40" y="58" fill="#24408E" font-size="24" font-weight="700" letter-spacing="3" style="{SANS}">{escape(T["head"])}</text>')
    b.append(f'<text x="{W - 40}" y="58" fill="#24408E" fill-opacity=".6" font-size="12" letter-spacing="2" text-anchor="end" style="{SANS}">{escape(T["ch"])}</text>')
    y = 104
    for label, value in T['fields']:
        if label:
            b.append(f'<text x="40" y="{y}" fill="#24408E" fill-opacity=".7" font-size="11" letter-spacing="2" style="{SANS}">{escape(label)}</text>')
            y += 22
        else:
            y -= 2
        b.append(f'<text x="40" y="{y}" fill="#1B1F2A" font-size="18" font-weight="700" style="{MONO}">{escape(value)}</text>')
        y += 34
    # stamps
    inks = ['#24408E', '#1F7AB8', '#8A5A2B', '#C8323C', '#6B3FA0', '#2E7D4F']
    spots = [  # cx, cy, rotation, shape, w, h (w grows to fit the text)
        (505, 150, -7, 'rect', 220, 118), (684, 148, 9, 'circle', 146, 146), (834, 168, 6, 'rect', 128, 96),
        (505, 318, 6, 'oval', 200, 118), (684, 322, -11, 'circle', 146, 146), (834, 316, -5, 'rect', 128, 112),
    ]
    for i, ((cx, cy, rot, shape, w, h), ink, lines) in enumerate(zip(spots, inks, T['stamps'])):
        need = max(len(t) * (8.6 if j else 17.5) for j, t in enumerate(lines)) + 30
        w = max(w, need)
        if shape == 'circle':
            h = w
        g = [f'<g transform="translate({cx} {cy}) rotate({rot})"><g class="stamp" style="animation-delay:{0.4 + i * 0.55:.2f}s" '
             f'filter="url(#ink)" fill="none" stroke="{ink}">']
        if shape == 'rect':
            g.append(f'<rect x="{-w / 2}" y="{-h / 2}" width="{w}" height="{h}" rx="8" stroke-width="4"/>')
            g.append(f'<rect x="{-w / 2 + 7}" y="{-h / 2 + 7}" width="{w - 14}" height="{h - 14}" rx="4" stroke-width="1.5"/>')
        elif shape == 'circle':
            g.append(f'<circle r="{w / 2}" stroke-width="4"/><circle r="{w / 2 - 8}" stroke-width="1.5"/>')
        else:
            g.append(f'<ellipse rx="{w / 2}" ry="{h / 2}" stroke-width="4"/><ellipse rx="{w / 2 - 8}" ry="{h / 2 - 8}" stroke-width="1.5"/>')
        n = len(lines)
        sizes = [26] + [13] * (n - 1)
        total = sum(sizes) + 6 * (n - 1)
        ty = -total / 2
        for j, (line, size) in enumerate(zip(lines, sizes)):
            ty += size
            g.append(f'<text y="{ty - 2:.1f}" fill="{ink}" stroke="none" font-size="{size}" font-weight="700" '
                     f'text-anchor="middle" letter-spacing="{2 if j == 0 else 1}" style="{SANS}">{escape(line)}</text>')
            ty += 6
        g.append('</g></g>')
        b.append(''.join(g))
    # machine-readable zone
    mrz = ['EXP<<KICH<MATA<<OTAVIO<<<<<<<<<<<<<<', 'RI<UFSC<<DPU<<UNV<<UFSCMUN<<<<<<<<<<']
    b.append(f'<rect x="20" y="{H - 92}" width="{W - 40}" height="70" fill="#FFFFFF" fill-opacity=".35"/>')
    for i, line in enumerate(mrz):
        b.append(f'<text x="40" y="{H - 62 + i * 28}" fill="#1B1F2A" font-size="21" letter-spacing="3.2" style="{MONO}">{escape(line)}</text>')
    defs = ('<defs><filter id="ink" x="-10%" y="-10%" width="120%" height="120%">'
            '<feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="4" result="n"/>'
            '<feDisplacementMap in="SourceGraphic" in2="n" scale="2.4" xChannelSelector="R" yChannelSelector="G" result="d"/>'
            '<feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 2.2 -.55" result="m"/>'
            '<feComposite in="d" in2="m" operator="in"/></filter></defs>')
    style = ('.stamp{opacity:0;transform-box:fill-box;transform-origin:center;animation:thump 15s ease-out infinite}'
             '@keyframes thump{0%{opacity:0;transform:scale(1.7)}2.4%{opacity:.92;transform:scale(.95)}'
             '3.6%{transform:scale(1)}86%{opacity:.92}92%{opacity:0}100%{opacity:0}}'
             '@media (prefers-reduced-motion:reduce){.stamp{animation:none;opacity:.92}}')
    return svg(W, H, defs + ''.join(b), T['aria'], style)


# ---------------------------------------------------------------- character sheet (CH 09)
SHEET_TEXT = {
    'en': {'menu': ['STATUS', 'QUESTS', 'FEATS', 'ITEMS'], 'cls': 'IR SCHOLAR + GAME DEV (MULTICLASS)',
           'place': 'FLORIANÓPOLIS, SC',
           'stats': [('GPA', '9.07 / 10'), ('LANGUAGES', '6'), ('GAMES MADE', '3'),
                     ('ARTICLES', '2'), ('MODEL UNS RUN', '2'), ('MATH OLYMPIAD', '2')],
           'quests': 'QUESTS', 'done': 'DONE', 'active': 'ACTIVE',
           'list': [('DPU MIGRATION UNIT · 2024–25', 0), ('UN ONLINE VOLUNTEER · 2024', 0),
                    ('IFSC TUTORING + RESEARCH · 2020–22', 0), ('BA IN IR AT UFSC · TO 2027', 1),
                    ('SOUTH-SOUTH RESEARCH · 2026', 1), ('KAPI ONLINE · SINCE 07·2026', 1)],
           'aria': 'An RPG status screen: GPA 9.07, six languages, three games made, two articles, and my quests'},
    'pt': {'menu': ['STATUS', 'MISSÕES', 'CONQUISTAS', 'ITENS'], 'cls': 'INTERNACIONALISTA + DEV DE JOGOS',
           'place': 'FLORIANÓPOLIS, SC · MULTICLASSE',
           'stats': [('IAA', '9,07 / 10'), ('IDIOMAS', '6'), ('JOGOS FEITOS', '3'),
                     ('ARTIGOS', '2'), ('ONUS SIMULADAS', '2'), ('OBMEP', '2')],
           'quests': 'MISSÕES', 'done': 'CONCLUÍDA', 'active': 'EM CURSO',
           'list': [('NÚCLEO DE MIGRAÇÃO DA DPU · 2024–25', 0), ('VOLUNTÁRIO ONLINE DA ONU · 2024', 0),
                    ('MONITORIA E PESQUISA NO IFSC · 2020–22', 0), ('RI NA UFSC · ATÉ 2027', 1),
                    ('PESQUISA SUL-SUL · 2026', 1), ('KAPI ONLINE · DESDE 07·2026', 1)],
           'aria': 'Uma tela de status de RPG: IAA 9,07, seis idiomas, três jogos feitos, dois artigos e as minhas missões'},
}


def window(x, y, w, h):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="url(#win)"/>'
            f'<rect x="{x + 3}" y="{y + 3}" width="{w - 6}" height="{h - 6}" rx="8" fill="none" stroke="#F4F6F6" stroke-width="5"/>'
            f'<rect x="{x + 8}" y="{y + 8}" width="{w - 16}" height="{h - 16}" rx="5" fill="none" stroke="#8B95C9" stroke-width="2"/>')


def sheet(lang):
    T = SHEET_TEXT[lang]
    W, H = 900, 470
    b = [f'<rect width="{W}" height="{H}" rx="14" fill="#0B0F2A"/>']
    b.append(window(16, 16, 190, 200))
    for i, item in enumerate(T['menu']):
        b.append(ptext(item, 60, 46 + i * 40, 2, '#F4F6F6' if i == 0 else '#B8C0E8', shadow='#0B0F2A'))
    b.append(f'<g class="cursor">{ptext("▶", 36, 46, 2, "#FFD866", shadow="#0B0F2A")}</g>')
    b.append(window(16, 228, 190, 226))
    b.append(f'<image href="data:image/svg+xml;base64,{TV_B64}" x="47" y="252" width="128" height="128" style="image-rendering:pixelated"/>')
    b.append(ptext('CH 09', 111, 404, 2, '#B8C0E8', anchor='middle', shadow='#0B0F2A'))
    b.append(ptext('KICH.DEV.BR', 111, 426, 2, '#FFD866', anchor='middle', shadow='#0B0F2A'))
    b.append(window(218, 16, 666, 438))
    X = 246
    b.append(ptext('OTÁVIO KICH MATA', X, 46, 3, '#F4F6F6', shadow='#0B0F2A'))
    b.append(ptext(T['cls'], X, 82, 2, '#FFD866', shadow='#0B0F2A'))
    b.append(ptext(T['place'], X, 104, 2, '#B8C0E8', shadow='#0B0F2A'))
    # stats in two columns
    for i, (k, v) in enumerate(T['stats']):
        cx = X + (i // 3) * 318
        cy = 140 + (i % 3) * 30
        b.append(ptext(k, cx, cy, 2, '#B8C0E8', shadow='#0B0F2A'))
        b.append(ptext(v, cx + 290, cy, 2, '#F4F6F6', shadow='#0B0F2A', anchor='end'))
    # GPA bar
    b.append(f'<rect x="{X}" y="232" width="290" height="10" fill="#0B0F2A" stroke="#8B95C9"/>')
    b.append(f'<rect class="bar" x="{X + 2}" y="234" width="{286 * 0.907:.1f}" height="6" fill="#6FD08C"/>')
    b.append(f'<line x1="{X}" y1="262" x2="{X + 610}" y2="262" stroke="#8B95C9" stroke-width="2"/>')
    b.append(ptext(T['quests'], X, 278, 2, '#FFD866', shadow='#0B0F2A'))
    for i, (q, active) in enumerate(T['list']):
        yy = 306 + i * 23
        b.append(ptext(q, X, yy, 2, '#F4F6F6', shadow='#0B0F2A'))
        tag = T['active'] if active else T['done']
        col = '#6FD08C' if active else '#8B95C9'
        cls = 'pulse' if active else ''
        b.append(ptext(tag, X + 610, yy, 2, col, shadow='#0B0F2A', anchor='end', cls=cls))
    defs = ('<defs><linearGradient id="win" x1="0" y1="0" x2="0" y2="1">'
            '<stop offset="0" stop-color="#3A54C8"/><stop offset="1" stop-color="#121D6E"/></linearGradient></defs>')
    style = ('.cursor{animation:bob .9s steps(2) infinite}@keyframes bob{50%{transform:translateX(5px)}}'
             '.bar{transform-box:fill-box;transform-origin:left;animation:fill 1.6s ease-out both .4s}'
             '@keyframes fill{from{transform:scaleX(0)}}'
             '.pulse{animation:pulse 2.4s ease-in-out infinite}@keyframes pulse{50%{opacity:.45}}'
             '@media (prefers-reduced-motion:reduce){.cursor,.bar,.pulse{animation:none}}')
    return svg(W, H, defs + ''.join(b), T['aria'], style)


# ---------------------------------------------------------------- items (CH 09, the RPG menu's ITEMS page)
ICONS = {
    'server': ['########', '#......#', '#.##...#', '########', '#......#', '#.##...#', '########', '........'],
    'palette': ['..####..', '.#....#.', '#.#..#.#', '#......#', '#..##..#', '#......#', '.#....#.', '..####..'],
    'cube': ['...##...', '..#..#..', '.#....#.', '#.#..#.#', '#..##..#', '#...#..#', '.#..#.#.', '..###...'],
    'db': ['.######.', '#......#', '.######.', '#......#', '.######.', '#......#', '.######.', '........'],
    'scroll': ['.######.', '#.#....#', '.#.###.#', '.#.....#', '.#.###.#', '.#.....#', '#.#....#', '.######.'],
    'chart': ['.......#', '......##', '...#..##', '..##.###', '.###.###', '########', '........', '........'],
    'spider': ['#..##..#', '.#.##.#.', '..####..', '########', '..####..', '.#.##.#.', '#......#', '........'],
    'plug': ['..#..#..', '..#..#..', '.######.', '.######.', '..####..', '...##...', '...##...', '...##...'],
    'globe': ['..####..', '.#.##.#.', '#..##..#', '########', '#..##..#', '.#.##.#.', '..####..', '........'],
}
ITEMS = [  # icon, colour, name, English effect, Portuguese effect
    ('server', '#46B154', 'NODE.JS', 'GAME SERVER, 30 TICKS/S', 'SERVIDOR DO JOGO, 30 TICKS/S'),
    ('palette', '#E8667A', 'CANVAS 2D + WEBGL2', 'ART DRAWN IN CODE', 'ARTE DESENHADA EM CÓDIGO'),
    ('cube', '#7FA6E8', 'GODOT 4', 'THE 3D CLIENT', 'O CLIENTE 3D'),
    ('db', '#C9713F', 'MONGODB', 'PLAYER DATA', 'DADOS DOS JOGADORES'),
    ('scroll', '#EDC04E', 'PYTHON', 'MICRODATA + POWER BI FILES', 'MICRODADOS + POWER BI'),
    ('chart', '#F2C94C', 'POWER BI + DAX', 'DASHBOARDS', 'PAINÉIS'),
    ('spider', '#A3ACB3', 'PLAYWRIGHT', 'THE MOODLE SCRAPER', 'O SCRAPER DO MOODLE'),
    ('plug', '#D98A4E', 'SOCKET.IO', 'REAL-TIME MULTIPLAYER', 'MULTIJOGADOR EM TEMPO REAL'),
    ('globe', '#6FB2E6', 'NGINX', 'SERVES MY SITES', 'SERVE OS MEUS SITES'),
]


def items(lang):
    W, H = 900, 346
    title = 'ITEMS' if lang == 'en' else 'ITENS'
    aria = ('An RPG items menu listing my tools: Node.js, Canvas 2D and WebGL2, Godot 4, MongoDB, '
            'Python, Power BI with DAX, Playwright, Socket.IO and nginx') if lang == 'en' else (
            'Um menu de itens de RPG com as minhas ferramentas: Node.js, Canvas 2D e WebGL2, Godot 4, MongoDB, '
            'Python, Power BI com DAX, Playwright, Socket.IO e nginx')
    b = [f'<rect width="{W}" height="{H}" rx="14" fill="#0B0F2A"/>', window(16, 16, W - 32, H - 32)]
    b.append(ptext(title, 46, 44, 3, '#FFD866', shadow='#0B0F2A'))
    b.append(ptext(f'{len(ITEMS)} / 99', W - 46, 48, 2, '#B8C0E8', shadow='#0B0F2A', anchor='end'))
    b.append(f'<line x1="44" y1="78" x2="{W - 44}" y2="78" stroke="#8B95C9" stroke-width="2"/>')
    for i, (icon, col, name, en, pt) in enumerate(ITEMS):
        x = 46 + (i // 5) * 418
        y = 96 + (i % 5) * 46
        b.append(f'<rect x="{x}" y="{y}" width="36" height="36" rx="4" fill="#0B0F2A" fill-opacity=".55" stroke="#8B95C9"/>')
        pts = [(c, r) for r, line in enumerate(ICONS[icon]) for c, ch in enumerate(line) if ch == '#']
        b.append(f'<g class="it" style="animation-delay:{i * 0.12:.2f}s">{pix(pts, col, x + 6, y + 6, 3)}</g>')
        b.append(ptext(name, x + 50, y + 2, 2, '#F4F6F6', shadow='#0B0F2A'))
        b.append(ptext(en if lang == 'en' else pt, x + 50, y + 22, 2, '#B8C0E8', shadow='#0B0F2A'))
    defs = ('<defs><linearGradient id="win" x1="0" y1="0" x2="0" y2="1">'
            '<stop offset="0" stop-color="#3A54C8"/><stop offset="1" stop-color="#121D6E"/></linearGradient></defs>')
    style = ('.it{animation:glint 6s ease-in-out infinite}@keyframes glint{0%,88%,100%{opacity:1}94%{opacity:.35}}'
             '@media (prefers-reduced-motion:reduce){.it{animation:none}}')
    return svg(W, H, defs + ''.join(b), aria, style)


# ---------------------------------------------------------------- War dice (CH 01, played through issues)
DICE_TEXT = {
    'en': {'atk': 'ATTACK', 'def': 'DEFENCE', 'capy': 'CAPYBARA', 'you': 'YOU',
           'line': 'ATTACK {a} × {d} DEFENCE', 'win': 'THE ATTACK WINS', 'hold': 'THE DEFENCE HOLDS',
           'none1': 'YOUR TURN.', 'none2': 'CLICK THE DICE TO ROLL',
           'score': 'VISITORS {v} · CAPYBARA {c}', 'rule': 'TIES GO TO THE DEFENCE, AS IN WAR',
           'aria': 'War dice against the capybara. {s}'},
    'pt': {'atk': 'ATAQUE', 'def': 'DEFESA', 'capy': 'CAPIVARA', 'you': 'VOCÊ',
           'line': 'ATAQUE {a} × {d} DEFESA', 'win': 'O ATAQUE LEVA', 'hold': 'A DEFESA SEGURA',
           'none1': 'SUA VEZ.', 'none2': 'CLIQUE NOS DADOS PARA ROLAR',
           'score': 'VISITANTES {v} · CAPIVARA {c}', 'rule': 'EMPATE FICA COM A DEFESA, COMO NO WAR',
           'aria': 'Dados de War contra a capivara. {s}'},
}


def die(colour, face, x, y, s):
    groups = {}
    for r, line in enumerate(ROOM['dice'][colour][str(face)]):
        for c, ch in enumerate(line):
            groups.setdefault(ROOM['pal'][ch], []).append((c, r))
    return ''.join(pix(v, col, x, y, s) for col, v in groups.items())


def dice_card(lang, state):
    T = DICE_TEXT[lang]
    W, H = 900, 226
    last = state['rolls'][0] if state['rolls'] else None
    red, yel = (last['red'], last['yellow']) if last else (6, 2)  # the room's dice at rest
    b = [f'<rect width="{W}" height="{H}" rx="14" fill="#10242B"/>',
         f'<rect x="12" y="12" width="{W - 24}" height="{H - 24}" rx="10" fill="#0A171C"/>']
    for colour, final, x, order in (('red', red, 130, [3, 6, 1, 4, 2, 5]), ('yel', yel, 700, [5, 2, 6, 1, 4, 3])):
        for k, face in enumerate(order):
            b.append(f'<g class="spin" style="animation-delay:{k * 0.16:.2f}s">{die(colour, face, x, 48, 10)}</g>')
        b.append(f'<g class="final">{die(colour, final, x, 48, 10)}</g>')
    capy = []
    for y, line in enumerate(ROOM['capybara']):
        for x, ch in enumerate(line):
            if ch != '.':
                capy.append(((x, y), ROOM['pal'][ch]))
    by_col = {}
    for p, col in capy:
        by_col.setdefault(col, []).append(p)
    b.append(''.join(pix(v, col, 628, 82, 2) for col, v in by_col.items()))
    who = ('@' + last['login'])[:17].upper() if last else T['you']
    b.append(ptext(who, 165, 138, 2, '#E8483C', anchor='middle'))
    b.append(ptext(T['atk'], 165, 162, 2, '#6E767C', anchor='middle'))
    b.append(ptext(T['capy'], 700, 138, 2, '#EDC04E', anchor='middle'))
    b.append(ptext(T['def'], 700, 162, 2, '#6E767C', anchor='middle'))
    if last:
        b.append(ptext(T['line'].format(a=red, d=yel), 425, 50, 3, '#F2E6B6', anchor='middle', shadow='#4A2412'))
        verdict = T['win'] if red > yel else T['hold']
        b.append(f'<g class="final">{ptext(verdict, 425, 86, 3, "#E8483C" if red > yel else "#EDC04E", anchor="middle")}</g>')
    else:
        b.append(ptext(T['none1'], 425, 50, 3, '#F2E6B6', anchor='middle', shadow='#4A2412'))
        b.append(ptext(T['none2'], 425, 88, 2, '#46B154', anchor='middle'))
    b.append(ptext(T['score'].format(v=state['visitors'], c=state['capybara']), 425, 128, 2, '#A3ACB3', anchor='middle'))
    b.append(ptext(T['rule'], W // 2, 196, 2, '#46B154', anchor='middle'))
    summary = (T['line'].format(a=red, d=yel) + ', ' + (T['win'] if red > yel else T['hold'])).capitalize() if last else T['none1']
    style = ('.spin{opacity:0;animation:spin 9s step-end infinite}'
             '@keyframes spin{0%{opacity:1}1.78%{opacity:0}100%{opacity:0}}'
             '.final{opacity:0;animation:land 9s step-end infinite}'
             '@keyframes land{0%{opacity:0}10.7%{opacity:1}100%{opacity:1}}'
             '@media (prefers-reduced-motion:reduce){.spin{animation:none}.final{animation:none;opacity:1}}')
    return svg(W, H, ''.join(b), T['aria'].format(s=summary), style)


def verdict(red, yellow, lang):
    if lang == 'en':
        return 'the attack wins' if red > yellow else 'the defence holds'
    return 'o ataque leva' if red > yellow else 'a defesa segura'


def dice_board(lang, state):
    """The scoreboard under the dice, between the <!-- dice --> markers."""
    v, c, total = state['visitors'], state['capybara'], state.get('total', 0)
    if not state['rolls']:
        return ('Nobody has rolled yet. Visitors 0, capybara 0.' if lang == 'en'
                else 'Ninguém rolou ainda. Visitantes 0, capivara 0.')
    if lang == 'en':
        lines = [f'Visitors {v}, capybara {c}, after {total} {"roll" if total == 1 else "rolls"}. The latest:', '',
                 '| Player | Attack | Defence | Result |', '| :-- | :-: | :-: | :-- |']
    else:
        lines = [f'Visitantes {v}, capivara {c}, depois de {total} {"rolagem" if total == 1 else "rolagens"}. '
                 'As últimas:', '', '| Jogador | Ataque | Defesa | Resultado |', '| :-- | :-: | :-: | :-- |']
    for r in state['rolls'][:5]:
        lines.append(f'| [{r["login"]}](https://github.com/{r["login"]}) | {r["red"]} | {r["yellow"]} | '
                     f'{verdict(r["red"], r["yellow"], lang)} |')
    return '\n'.join(lines)


# ---------------------------------------------------------------- end of broadcast (CH 11)
END_TEXT = {
    'en': {'big': 'END OF BROADCAST', 'aria': 'Test-pattern colour bars with the words End of broadcast, then the tube switches off'},
    'pt': {'big': 'FIM DE TRANSMISSÃO', 'aria': 'Barras de cor do padrão de teste com as palavras Fim de transmissão, e o tubo se apaga'},
}


def endcard(lang):
    T = END_TEXT[lang]
    W, H = 900, 260
    sx, sy, sw, sh = 24, 20, W - 48, H - 40
    b = [f'<rect width="{W}" height="{H}" rx="14" fill="#050607"/>']
    s = ['<g class="tube">']
    bw = sw / 7
    for i, c in enumerate(BARS):
        s.append(f'<rect x="{sx + i * bw:.1f}" y="{sy}" width="{bw + .5:.1f}" height="{sh * .68:.1f}" fill="{c}"/>')
    mid = ['#0000C0', '#131313', '#C000C0', '#131313', '#00C0C0', '#131313', '#C0C0C0']
    for i, c in enumerate(mid):
        s.append(f'<rect x="{sx + i * bw:.1f}" y="{sy + sh * .68:.1f}" width="{bw + .5:.1f}" height="{sh * .08:.1f}" fill="{c}"/>')
    low = [('#00214C', 1.25), ('#FFFFFF', 1.25), ('#32006A', 1.25), ('#131313', 1.25), ('#090909', .34), ('#131313', .33), ('#1D1D1D', .35)]
    x = sx
    for c, f in low:
        s.append(f'<rect x="{x:.1f}" y="{sy + sh * .76:.1f}" width="{bw * f + .5:.1f}" height="{sh * .24:.1f}" fill="{c}"/>')
        x += bw * f
    tw = text_width(T['big'], 4) + 48
    s.append(f'<rect x="{(W - tw) / 2:.1f}" y="{sy + 44}" width="{tw:.1f}" height="76" fill="#050607"/>')
    s.append(ptext(T['big'], W // 2, sy + 60, 4, '#F4F6F6', anchor='middle'))
    s.append(ptext('KICH.DEV.BR', W // 2, sy + 98, 2, '#EDC04E', anchor='middle'))
    s.append(f'<rect class="flash" x="{sx}" y="{sy}" width="{sw}" height="{sh}" fill="#FFFFFF"/>')
    s.append('</g>')
    b.append(f'<g class="tv">{"".join(s)}</g>')
    b.append(f'<circle class="dot" cx="{W / 2}" cy="{H / 2}" r="5" fill="#FFFFFF"/>')
    style = (f'.tv{{transform-origin:{W / 2}px {H / 2}px;animation:off 10s ease-in-out infinite}}'
             '@keyframes off{0%,70%{transform:scale(1,1);opacity:1}74%{transform:scale(1,.012)}'
             '78%{transform:scale(.002,.012);opacity:1}80%{transform:scale(0,0);opacity:0}'
             '93%{transform:scale(0,0);opacity:0}95%{transform:scale(1,.012);opacity:1}100%{transform:scale(1,1)}}'
             '.flash{opacity:0;animation:fl 10s infinite}@keyframes fl{0%,70%{opacity:0}74%,78%{opacity:.9}95%{opacity:.9}100%{opacity:0}}'
             '.dot{opacity:0;animation:dot 10s infinite}@keyframes dot{0%,77%{opacity:0}79%{opacity:1}88%{opacity:0}100%{opacity:0}}'
             '@media (prefers-reduced-motion:reduce){.tv,.flash,.dot{animation:none}}')
    return svg(W, H, ''.join(b), T['aria'], style)


# ---------------------------------------------------------------- map (CH 06)
# Records 2010 to Apr 2026, Global South under the UN DESA definition, from
# docs/dados.json of github.com/tavmata/painel-sul-sul-sismigra.
# (iso3, English, Portuguese, region, lon, lat, records, % work/investment, % humanitarian or refuge)
ORIGINS = [
    ('CHN', 'China', 'China', 'asia', 116.40, 39.90, 64990, 42.9, 4.7),
    ('PHL', 'Philippines', 'Filipinas', 'asia', 120.98, 14.60, 26271, 93.6, 1.5),
    ('IND', 'India', 'Índia', 'asia', 77.21, 28.61, 22670, 81.9, 2.2),
    ('KOR', 'South Korea', 'Coreia do Sul', 'asia', 126.98, 37.57, 17300, 58.9, 1.0),
    ('SYR', 'Syria', 'Síria', 'asia', 36.29, 33.51, 8984, 0.7, 49.1),
    ('BGD', 'Bangladesh', 'Bangladesh', 'asia', 90.41, 23.81, 7797, 23.9, 19.2),
    ('AFG', 'Afghanistan', 'Afeganistão', 'asia', 69.21, 34.56, 7627, 0.2, 97.8),
    ('LBN', 'Lebanon', 'Líbano', 'asia', 35.50, 33.89, 6973, 3.3, 25.2),
    ('IDN', 'Indonesia', 'Indonésia', 'asia', 106.85, -6.21, 6476, 92.6, 0.3),
    ('TUR', 'Turkey', 'Turquia', 'asia', 32.86, 39.93, 3385, 32.9, 7.1),
    ('AGO', 'Angola', 'Angola', 'africa', 13.23, -8.84, 33029, 1.6, 49.4),
    ('SEN', 'Senegal', 'Senegal', 'africa', -17.47, 14.72, 10967, 8.4, 5.5),
    ('NGA', 'Nigeria', 'Nigéria', 'africa', 7.40, 9.08, 8264, 5.1, 21.2),
    ('GNB', 'Guinea-Bissau', 'Guiné-Bissau', 'africa', -15.60, 11.86, 7379, 2.3, 13.7),
    ('MOZ', 'Mozambique', 'Moçambique', 'africa', 32.57, -25.97, 6025, 9.5, 6.7),
    ('MAR', 'Morocco', 'Marrocos', 'africa', -6.83, 34.02, 4821, 4.0, 54.3),
    ('GHA', 'Ghana', 'Gana', 'africa', -0.19, 5.60, 4140, 5.1, 40.0),
    ('EGY', 'Egypt', 'Egito', 'africa', 31.24, 30.04, 3474, 13.3, 15.6),
    ('CPV', 'Cape Verde', 'Cabo Verde', 'africa', -23.51, 14.93, 3143, 2.6, 4.4),
    ('COD', 'DR Congo', 'RD Congo', 'africa', 15.27, -4.44, 2780, 1.5, 54.2),
]
BRASILIA = (-47.88, -15.79)


def num(n, pt):
    return f'{n:,}'.replace(',', '.') if pt else f'{n:,}'


def pct(v, pt):
    return f'{v:.1f}%'.replace('.', ',') if pt else f'{v:.1f}%'


def geojson(lang):
    """Origins as points, each joined to Brazil by a line. GitHub's map ignores
    simplestyle colours, so the data carries only what a reader needs."""
    pt = lang == 'pt'
    reg = {'asia': 'Ásia' if pt else 'Asia', 'africa': 'África' if pt else 'Africa'}
    feats = []
    for iso, en, ptn, r, lon, lat, n, work, hum in ORIGINS:
        label = {'de': ptn, 'registros': num(n, pt)} if pt else {'from': en, 'records': num(n, pt)}
        feats.append({'type': 'Feature', 'geometry': {'type': 'LineString', 'coordinates': [[lon, lat], list(BRASILIA)]},
                      'properties': label})
    for iso, en, ptn, r, lon, lat, n, work, hum in ORIGINS:
        if pt:
            props = {'país': ptn, 'região': reg[r], 'registros': num(n, pt),
                     'amparo de trabalho ou investimentos': pct(work, pt), 'acolhida humanitária ou refúgio': pct(hum, pt)}
        else:
            props = {'country': en, 'region': reg[r], 'records': num(n, pt),
                     'work or investment basis': pct(work, pt), 'humanitarian or refugee basis': pct(hum, pt)}
        feats.append({'type': 'Feature', 'geometry': {'type': 'Point', 'coordinates': [lon, lat]}, 'properties': props})
    feats.append({'type': 'Feature', 'geometry': {'type': 'Point', 'coordinates': list(BRASILIA)},
                  'properties': {'name': 'Brasil' if pt else 'Brazil'}})
    return {'type': 'FeatureCollection', 'features': feats}


def table(lang):
    """The numbers behind the map, as a Markdown table sorted by records."""
    pt = lang == 'pt'
    head = (['País', 'Região', 'Registros', 'Trabalho ou investimentos', 'Acolhida humanitária ou refúgio'] if pt else
            ['Country', 'Region', 'Records', 'Work or investment basis', 'Humanitarian or refugee basis'])
    reg = {'asia': 'Ásia' if pt else 'Asia', 'africa': 'África' if pt else 'Africa'}
    rows = ['| ' + ' | '.join(head) + ' |', '| :-- | :-- | --: | --: | --: |']
    for iso, en, ptn, r, lon, lat, n, work, hum in sorted(ORIGINS, key=lambda o: -o[6]):
        rows.append(f'| {ptn if pt else en} | {reg[r]} | {num(n, pt)} | {pct(work, pt)} | {pct(hum, pt)} |')
    return '\n'.join(rows)


def fill(readme, marker, content):
    """Replaces the text between <!-- marker:start --> and <!-- marker:end -->."""
    p = ROOT / readme
    s = p.read_text(encoding='utf-8')
    a, b = f'<!-- {marker}:start -->', f'<!-- {marker}:end -->'
    i, j = s.index(a) + len(a), s.index(b)
    p.write_text(s[:i] + '\n' + content + '\n' + s[j:], encoding='utf-8')


def main():
    global TV_B64
    import base64
    TV_B64 = base64.b64encode((ROOT / 'tools' / 'tv32.svg').read_bytes()).decode()
    ASSETS.mkdir(exist_ok=True)
    for lang in ('en', 'pt'):
        write(f'header-{lang}.svg', header(lang))
        write(f'passport-{lang}.svg', passport(lang))
        write(f'sheet-{lang}.svg', sheet(lang))
        write(f'end-{lang}.svg', endcard(lang))
        write(f'items-{lang}.svg', items(lang))
        state = json.loads((ROOT / 'game' / 'state.json').read_text(encoding='utf-8'))
        write(f'dice-{lang}.svg', dice_card(lang, state))
        readme = 'README.md' if lang == 'en' else 'README.pt-BR.md'
        fill(readme, 'dice', dice_board(lang, state))
        g = json.dumps(geojson(lang), ensure_ascii=False, separators=(',', ':'))
        fill(readme, 'map', f'```geojson\n{g}\n```')
        fill(readme, 'table', table(lang))


TV_B64 = ''

if __name__ == '__main__':
    main()
