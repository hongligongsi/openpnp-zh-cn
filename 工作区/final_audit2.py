# -*- coding: utf-8 -*-
"""final_audit2.py — 收紧过滤：只挑真正的“英文句子”型可见文案。"""
import sys, zipfile, io, re, json, collections
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.')
import class_patch

JAR = r'C:\Program Files\openpnp\openpnp-gui-0.0.1-alpha-SNAPSHOT.jar'

def has_cjk(s):
    return any('\u4e00' <= c <= '\u9fff' for c in s)

LOWER_START = re.compile(r'^[a-z]')
# 常见 Java 库/框架字符串特征
LIB_PAT = re.compile(
    r'(^[a-z]+(\.[a-z0-9]+)+$)'          # 全小写点分（包名/域名）
    r'|(^[A-Z][a-zA-Z0-9]*(\.[A-Za-z0-9]+)+$)'   # 类全名
    r'|(java\.|javax\.|sun\.|com\.sun)'
    r'|(0x[0-9a-fA-F])'
    r'|(\{[^}]*\})'                       # 花括号模板
    r'|(%[-#0-9.]*[a-zA-Z])'              # 格式符
)
# 英文句子必须具备的：>=2 个词、总长度 >= 12、且含一个 >=3 字母的词
WORD = re.compile(r'[A-Za-z]{2,}')

def is_sentence(s):
    if not s or has_cjk(s):
        return False
    st = s.strip()
    if len(st) < 12:
        return False
    words = WORD.findall(st)
    if len(words) < 3:
        return False
    # 若几乎全是标识符风格（含大量 . / $ / _）则跳过
    ident_like = sum(1 for c in st if c in './$\\_') / max(len(st), 1)
    if ident_like > 0.18:
        return False
    # 至少要有一个空格分隔的普通单词对
    if ' ' not in st:
        return False
    # 排除 HTML/SVG/CV-pipeline 大块（单独处理）
    low = st.lower()
    if low.startswith('<?xml') or low.startswith('<svg') or low.startswith('<cv-pipeline'):
        return False
    if low.startswith('<line') or low.startswith('<circle') or low.startswith('<text'):
        return False
    if low.startswith('<package') or low.startswith('<pad'):
        return False
    # 排除属性赋值型 (key=value key2=value2)
    if re.match(r'^[\w-]+="[^"]*"(\s+[\w-]+="[^"]*")*$', st):
        return False
    # 排除 OpenCV YAML
    if '%yaml' in low:
        return False
    # 排除 logback/日志 pattern
    if re.match(r'^\{[a-z_]+[:}]', st):
        return False
    return True

targets = []
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
            if is_sentence(s):
                targets.append((name, s))

print('候选英文句子：', len(targets))
print()

byclass = collections.OrderedDict()
for n, s in targets:
    byclass.setdefault(n.split('/')[-1], []).append(s)

total = 0
for cn, ss in sorted(byclass.items(), key=lambda x: -len(x[1])):
    total += len(ss)
    print('### %s  (%d)' % (cn, len(ss)))
    for s in ss:
        print('   ', repr(s)[:170])
    print()
print('总计:', total)
json.dump([[n, s] for n, s in targets],
          open('audit_targets.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
