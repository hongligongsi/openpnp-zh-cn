# -*- coding: utf-8 -*-
import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
d = json.load(open('sweep_en.json', encoding='utf-8'))
html = [s for s in d if s.lower().startswith('<html')]
print('HTML total', len(html))
for i, s in enumerate(html, 1):
    cls = d[s][0].split('/')[-1]
    print('[%d] %s' % (i, cls))
    print(repr(s))
    print()
