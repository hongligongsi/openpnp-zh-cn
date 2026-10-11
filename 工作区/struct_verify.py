# -*- coding: utf-8 -*-
"""struct_verify.py — 结构完整性校验：按 class 文件规范逐字节解析 CP → 字段 → 方法 → 属性。
对 ORIGINAL 与 PATCHED 各跑一遍，确认两者结构均合法（尤其确认是「修改前就合法」，
以排除工具本身的 bug 造成假阳性）。"""
import struct, zipfile, sys, collections

def parse(data, verbose=False):
    assert data[:4] == b'\xca\xfe\xba\xbe', 'magic'
    minor, major = struct.unpack('>HH', data[4:8])
    n = struct.unpack('>H', data[8:10])[0]
    i = 10; idx = 1
    tags = collections.Counter()
    while idx < n:
        tag = data[i]; tags[tag] += 1
        if tag == 1:
            ln = struct.unpack('>H', data[i+1:i+3])[0]; i += 3 + ln
        elif tag in (7,8,16,19,20): i += 3
        elif tag == 15: i += 4
        elif tag in (3,4,9,10,11,12,17,18): i += 5
        elif tag in (5,6): i += 9; idx += 1
        else: raise ValueError('cp tag %d @%d' % (tag, idx))
        idx += 1
    # access_flags, this_class, super_class, interfaces
    af, this_c, super_c, ic = struct.unpack('>HHHH', data[i:i+8]); i += 8
    i += 2 * ic
    def read_attrs(i):
        cnt = struct.unpack('>H', data[i:i+2])[0]; i += 2
        for _ in range(cnt):
            alen = struct.unpack('>I', data[i+2:i+6])[0]
            i += 6 + alen
        return i
    # fields
    fc = struct.unpack('>H', data[i:i+2])[0]; i += 2
    for _ in range(fc):
        i += 6
        i = read_attrs(i)
    # methods
    mc = struct.unpack('>H', data[i:i+2])[0]; i += 2
    for _ in range(mc):
        i += 6
        i = read_attrs(i)
    # class attrs
    i = read_attrs(i)
    return (n, i, len(data), major, tags)

def run(path, label):
    z = zipfile.ZipFile(path)
    ok = bad = 0; badlist = []
    for name in z.namelist():
        if not name.endswith('.class'): continue
        try:
            n, end, size, major, tags = parse(z.read(name))
            if end != size:
                bad += 1; badlist.append((name, 'len %d != %d' % (end, size)))
            else:
                ok += 1
        except Exception as e:
            bad += 1; badlist.append((name, str(e)[:60]))
    print('%s  OK: %d  BAD: %d' % (label.ljust(12), ok, bad))
    for n, m in badlist[:8]: print('    ', m, n)
    return ok, bad

for p, l in [(sys.argv[1], 'ORIGINAL'), (sys.argv[2], 'PATCHED')]:
    run(p, l)
