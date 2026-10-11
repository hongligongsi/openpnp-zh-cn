# -*- coding: utf-8 -*-
"""apply_all3.py — 第三轮：合并 batch11-14 残留汉化，重新生成最终 JAR。

基础：openpnp-gui-final.jar（已含 properties + Batch0..Batch10）
输出：openpnp-gui-final.jar（原地覆盖）
"""
import json, sys, zipfile, os, hashlib, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.')
import class_patch, translation_pipeline

BASE = 'openpnp-gui-final.jar'
TMP  = 'openpnp-gui-final.tmp.jar'

# 1) 载入既有全量映射（prototype § 形式）
base_map = json.load(open('final_repl.json', encoding='utf-8'))
print('既有映射:', len(base_map))

# 2) 载入本轮 batch11-14
from batch11_residual import TABLE as T11
from batch12_text import TABLE as T12
from batch13_text2 import TABLE as T13
from batch14_html2 import TABLE as T14

NEW = {}
for t in (T11, T12, T13, T14):
    for k, v in t.items():
        if k in NEW and NEW[k] != v:
            print('[冲突]', repr(k))
        NEW[k] = v
print('本轮新增:', len(NEW))

# 3) 合并（本轮优先覆盖）
MERGED = dict(base_map)
MERGED.update(NEW)
print('合并后总映射:', len(MERGED))

# 4) 校验并构建替换映射（真实字符串 -> 真实译文）
real = set()
zin = zipfile.ZipFile(BASE, 'r')
names = zin.namelist()
for n in names:
    if not n.endswith('.class'):
        continue
    d = zin.read(n)
    ent, _ = class_patch.parse_cp(d)
    real.update(class_patch.get_utf8(d, ent))
zin.close()

REPL, errs = translation_pipeline.build_replacement_map(MERGED, real)
print('可应用替换:', len(REPL), '校验问题:', len(errs))
for e in errs[:20]:
    print('  ', e)

# 5) 重建 JAR
zin = zipfile.ZipFile(BASE, 'r')
out = zipfile.ZipFile(TMP, 'w', zipfile.ZIP_DEFLATED)
tot_hit = 0
hit_classes = []
try:
    for name in names:
        data = zin.read(name)
        if name.endswith('.class'):
            try:
                nd, hit = class_patch.rebuild(data, REPL)
            except Exception as e:
                print('  [跳过]', name, e)
                nd, hit = data, 0
            if hit:
                tot_hit += hit
                hit_classes.append((name, hit))
            data = nd
        gi = zin.getinfo(name)
        zi = zipfile.ZipInfo(name, date_time=gi.date_time)
        zi.compress_type = gi.compress_type
        zi.external_attr = gi.external_attr
        zi.internal_attr = gi.internal_attr
        zi.create_system = gi.create_system
        zi.comment = gi.comment
        out.writestr(zi, data)
finally:
    out.close()
    zin.close()

os.replace(TMP, BASE)

print()
print('=== 第三轮应用结果 ===')
print('命中常量池条目总数 :', tot_hit)
print('被修改的 class 数  :', len(hit_classes))
for n, h in sorted(hit_classes, key=lambda x: -x[1])[:25]:
    print('   ', str(h).rjust(4), n)
print('输出:', BASE, os.path.getsize(BASE), 'bytes')
h = hashlib.sha256(open(BASE, 'rb').read()).hexdigest()
print('SHA256:', h)

json.dump(MERGED, open('final_repl.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
json.dump({'sha256': h, 'size': os.path.getsize(BASE), 'hit': tot_hit,
           'classes': len(hit_classes), 'map': len(MERGED), 'round': 3},
          open('final_build3.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=2)
print('写入 final_repl.json / final_build3.json')
