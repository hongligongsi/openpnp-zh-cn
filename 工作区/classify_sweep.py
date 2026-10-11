# -*- coding: utf-8 -*-
"""对 sweep_en.json 中的残留字符串分类，过滤出真正需要汉化的可见文案。"""
import json, re, collections, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

d = json.load(open('sweep_en.json', encoding='utf-8'))

def classify(s):
    low = s.lower().lstrip()
    if low.startswith('<html'):
        return 'HTML'
    if low.startswith('<?xml') or low.startswith('<cv-pipeline') or low.startswith('<'):
        return 'XML'
    if '%yaml' in low:
        return 'YAML'
    if re.match(r'^\{[A-Za-z]+:', s):
        return 'LOG-FMT'
    if re.match(r'^\{[A-Za-z]+:', s.strip('{')):
        return 'LOG-FMT'
    # G-code
    if re.search(r'(^|\s)(G\d+|M\d+)', s) and ('\n' in s or ';' in s or '{' in s):
        return 'GCODE'
    if re.match(r'^[a-z][A-Za-z0-9_]*\(\)', s):
        return 'JAVA-CALL'
    if re.search(r'\bnot implemented for\b', s):
        return 'JAVA-CALL'
    if re.match(r'^\{.*\}', s) and len(re.findall(r'[A-Za-z]', s)) < 30:
        return 'BRACE'
    return 'TEXT'

cats = collections.Counter()
for s in d:
    cats[classify(s)] += 1
for k, v in cats.most_common():
    print(k, v)

print()
print('=== TEXT 类明细 ===')
n = 0
for s in d:
    if classify(s) == 'TEXT':
        n += 1
        print('[%d] %r  <- %s' % (n, s, d[s][0].split('/')[-1]))
print('TEXT total', n)
