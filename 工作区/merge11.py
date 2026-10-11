# -*- coding: utf-8 -*-
"""合并 batch11/12/13 并检查覆盖率。"""
import sys, zipfile, json, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.')
import class_patch, translation_pipeline
from batch11_residual import TABLE as T11
from batch12_text import TABLE as T12
from batch13_text2 import TABLE as T13

MERGED = {}
for t in (T11, T12, T13):
    for k, v in t.items():
        if k in MERGED and MERGED[k] != v:
            print('[冲突]', repr(k))
        MERGED[k] = v
print('合并后条目:', len(MERGED))

sweep = json.load(open('sweep_en.json', encoding='utf-8'))
real = set()
with zipfile.ZipFile('openpnp-gui-final.jar') as z:
    for n in z.namelist():
        if not n.endswith('.class'):
            continue
        d = z.read(n)
        ent, _ = class_patch.parse_cp(d)
        real.update(class_patch.get_utf8(d, ent))

repl, errs = translation_pipeline.build_replacement_map(MERGED, real)
print('命中:', len(repl), '问题:', len(errs))
for e in errs:
    print('  ', e)

# 覆盖率：哪些 sweep 条目仍未翻译
covered = {s.replace('\x01', '§') for s in repl}
missing = [s for s in sweep if s.replace('\x01', '§') not in covered]
print()
print('sweep 中仍未覆盖:', len(missing))
json.dump(MERGED, open('b11_13_merged.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)

# 写一份未覆盖清单
with open('_still_missing.txt', 'w', encoding='utf-8') as f:
    for s in missing:
        f.write('%r\n' % s)
