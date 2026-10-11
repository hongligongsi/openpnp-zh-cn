# -*- coding: utf-8 -*-
"""final_audit.py — 全量审计：扫描 JAR 内所有 class 常量池 + properties，
找出所有仍含英文的“可见文案”（排除类名/URL/G代码/格式串等不可译项）。"""
import sys, zipfile, io, re, json, collections
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.')
import class_patch

JAR = r'C:\Program Files\openpnp\openpnp-gui-0.0.1-alpha-SNAPSHOT.jar'

def has_cjk(s):
    return any('\u4e00' <= c <= '\u9fff' for c in s)

# ---- 判定是否“可能是可见文案” ----
def looks_visible(s):
    if not s or not s.strip():
        return False
    if has_cjk(s):
        return False                      # 已含中文 → 已翻译
    if s.startswith('http://') or s.startswith('https://'):
        return False
    # 纯标识符 / 路径 / 类名
    if re.fullmatch(r'[\w./$\[\]<>-]+', s):
        return False
    # 含空格的标识符串（如 org.openpnp.model.Location）
    if re.fullmatch(r'[\w./$]+( +[\w./$]+)+', s):
        return False
    # 不是字母开头（数字、符号、格式符开头），且没有 3 个连续字母
    if len(re.findall(r'[A-Za-z]{3,}', s)) == 0:
        return False
    return True

targets = []          # (classname, string)
xml_only = []         # 纯标记/配置
with zipfile.ZipFile(JAR) as z:
    for name in sorted(z.namelist()):
        if not name.endswith('.class'):
            continue
        d = z.read(name)
        try:
            ent, _ = class_patch.parse_cp(d)
            strs = class_patch.get_utf8(d, ent)
        except Exception:
            continue
        for s in strs:
            if not looks_visible(s):
                continue
            low = s.lower().lstrip()
            # 归类
            if (low.startswith('<?xml') or low.startswith('<svg') or
                low.startswith('<cv-pipeline') or low.startswith('<line') or
                low.startswith('<circle') or low.startswith('<text') or
                low.startswith('<package') or low.startswith('<pad')):
                xml_only.append((name, s))
                continue
            if re.search(r'\b(org\.openpnp|java\.|javax\.|com\.|net\.)\w', s):
                xml_only.append((name, s))
                continue
            # 纯 SVG 样式串
            if re.fullmatch(r'[a-z-]+:\s*[\w#() ,;.%-]+;?', s):
                xml_only.append((name, s))
                continue
            targets.append((name, s))

print('=' * 70)
print('仍需人工判断的字符串：', len(targets))
print('=' * 70)

# 按类分组输出
byclass = collections.OrderedDict()
for n, s in targets:
    byclass.setdefault(n.split('/')[-1], []).append(s)

for cn, ss in sorted(byclass.items(), key=lambda x: -len(x[1])):
    print()
    print('### %s  (%d)' % (cn, len(ss)))
    for s in ss:
        print('   ', repr(s)[:160])

print()
print('=' * 70)
print('被排除（XML/SVG/类名/配置）：', len(xml_only))
print('=' * 70)

json.dump({'targets': [[n, s] for n, s in targets]},
          open('audit_targets.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
