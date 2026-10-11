# -*- coding: utf-8 -*-
import json, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
d = json.load(open('sweep_en.json', encoding='utf-8'))

def classify(s):
    low = s.lower().lstrip()
    if low.startswith('<html'): return 'HTML'
    if low.startswith('<?xml') or low.startswith('<cv-pipeline') or low.startswith('<'): return 'XML'
    if '%yaml' in low: return 'YAML'
    if re.match(r'^\{[A-Za-z]+:', s): return 'LOG-FMT'
    if re.search(r'(^|\s)(G\d+|M\d+)', s) and ('\n' in s or ';' in s or '{' in s): return 'GCODE'
    if re.match(r'^[a-z][A-Za-z0-9_]*\(\)', s): return 'JAVA-CALL'
    if re.search(r'\bnot implemented for\b', s): return 'JAVA-CALL'
    if re.match(r'^\{.*\}', s) and len(re.findall(r'[A-Za-z]', s)) < 30: return 'BRACE'
    return 'TEXT'

for want in ('XML','YAML','LOG-FMT','GCODE','JAVA-CALL','BRACE'):
    print('===== %s =====' % want)
    for s in d:
        if classify(s) == want:
            print(repr(s)[:200], '  <-', d[s][0].split('/')[-1])
    print()
