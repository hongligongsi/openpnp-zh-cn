# -*- coding: utf-8 -*-
"""apply_all.py — 将全部翻译映射应用到 JAR 中的 class 常量池。
在已安装（含 Batch0 + properties 汉化）的 JAR 基础上继续打补丁。
"""
import json, sys, zipfile, shutil, hashlib, os, io
sys.path.insert(0, '.')
import class_patch

SRC = r'C:\Program Files\openpnp\openpnp-gui-0.0.1-alpha-SNAPSHOT.jar'
WORK = 'openpnp-gui-patched.jar'        # 工作区中已含 Batch0 补丁的 jar
OUT  = 'openpnp-gui-final.jar'

# 1) 读取最终替换映射（prototype 是 § 形式，需要转成真实的 \x01）
proto = json.load(open('final_repl.json', encoding='utf-8'))
REPL = {k: v for k, v in proto.items()}           # 真实字符串 -> 真实译文
print('替换映射条数:', len(REPL))

# patch_map（Batch0）已在 jar 中应用过，这里补上它是为了自洽（幂等）
import patch_map
for attr in ('FULL', 'PARTIAL'):
    if hasattr(patch_map, attr):
        for k, v in getattr(patch_map, attr).items():
            REPL.setdefault(k, v)
print('含 Batch0 后总条数:', len(REPL))

src = WORK if os.path.exists(WORK) else SRC
print('基础 JAR:', src, os.path.getsize(src), 'bytes')

zin = zipfile.ZipFile(src, 'r')
names = zin.namelist()
classes = [n for n in names if n.endswith('.class')]
print('class 文件数:', len(classes))

out = zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED)
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
        zi = zipfile.ZipInfo(name, date_time=zin.getinfo(name).date_time)
        zi.compress_type = zin.getinfo(name).compress_type
        zi.external_attr = zin.getinfo(name).external_attr
        zi.internal_attr = zin.getinfo(name).internal_attr
        zi.create_system = zin.getinfo(name).create_system
        zi.comment = zin.getinfo(name).comment
        out.writestr(zi, data)
finally:
    out.close()
    zin.close()

print()
print('=== 应用结果 ===')
print('命中常量池条目总数 :', tot_hit)
print('被修改的 class 数  :', len(hit_classes))
for n, h in sorted(hit_classes, key=lambda x: -x[1])[:25]:
    print('   ', str(h).rjust(4), n)
print('输出:', OUT, os.path.getsize(OUT), 'bytes')
h = hashlib.sha256(open(OUT, 'rb').read()).hexdigest()
print('SHA256:', h)
json.dump({'sha256': h, 'size': os.path.getsize(OUT), 'hit': tot_hit,
           'classes': len(hit_classes), 'map': len(REPL)},
          open('final_build.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
