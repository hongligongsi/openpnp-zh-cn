# -*- coding: utf-8 -*-
"""列出候选：既有未翻译，也不在排除表中。"""
import json, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

d = json.load(open('sweep_en.json', encoding='utf-8'))

EXCLUDE = set()

# ---- XML / SVG / markup-only ----
for s in d:
    low = s.lower().lstrip()
    if low.startswith('<?xml'): EXCLUDE.add(s)
    elif low.startswith('<cv-pipeline'): EXCLUDE.add(s)
    elif low.startswith('<package id='): EXCLUDE.add(s)
    elif low.startswith('<pad '): EXCLUDE.add(s)
    elif re.match(r'^<line\b', low): EXCLUDE.add(s)
    elif re.match(r'^<circle\b', low): EXCLUDE.add(s)
    elif re.match(r'^<text\b', low): EXCLUDE.add(s)
    elif re.match(r'^<title>', low): EXCLUDE.add(s)
    elif re.match(r'^</p>', low): EXCLUDE.add(s)
    elif low in ('<html>', '<html/>', '<html>\n'): EXCLUDE.add(s)
    elif re.match(r'^<<<\s', low): EXCLUDE.add(s)

# ---- YAML / OpenCV config ----
for s in d:
    if '%yaml' in s.lower(): EXCLUDE.add(s)

# ---- Java identifier calls ----
for s in d:
    if re.match(r'^[a-z][A-Za-z0-9_]*\(\)', s): EXCLUDE.add(s)
    if re.match(r'^\{[A-Za-z]+:', s) and s.startswith('{date:'): EXCLUDE.add(s)

# ---- brace-only format strings ({}) with no real words ----
for s in d:
    if s.startswith('{}') or re.match(r'^\{[^ ]*\}\s', s):
        if len(re.findall(r'[A-Za-z]+', s)) <= 8: EXCLUDE.add(s)

# ---- pure G-code / numeric / template fragments ----
GCODE_RE = re.compile(r'^(G\d+|M\d+)')
for s in d:
    st = s.strip()
    if GCODE_RE.match(st) and re.search(r';|\\n|\{', s): EXCLUDE.add(s)

# ---- strings composed only of format specifiers and symbols ----
for s in d:
    core = re.sub(r'%[-#0-9.*]*[a-zA-Z]', '', s)
    core = re.sub(r'[\s,;:.\-+()\[\]{}=%°/]', '', core)
    if not core: EXCLUDE.add(s)

print('排除:', len(EXCLUDE))
cand = [s for s in d if s not in EXCLUDE]
print('候选:', len(cand))

# classify remaining for review
def kind(s):
    low = s.lower().lstrip()
    if low.startswith('<html'): return 'HTML'
    if low.startswith('<'): return 'XML'
    if re.search(r'(^|\s)[GM]\d+', s) and (';' in s or '\\n' in s): return 'GCODE'
    return 'TEXT'
import collections
c = collections.Counter(kind(s) for s in cand)
print(c)

with open('_cands.txt','w',encoding='utf-8') as f:
    for s in cand:
        f.write('%s\t%r\t%s\n' % (kind(s), s, d[s][0].split('/')[-1]))
print('written _cands.txt')
