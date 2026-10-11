# -*- coding: utf-8 -*-
"""count_zh.py — 统计 JAR 内 class 常量池含中文的条目数（供安装脚本调用）。
用法: python count_zh.py <jar路径>
"""
import sys, zipfile, struct, io

def count(jar):
    n = 0
    try:
        z = zipfile.ZipFile(jar)
    except Exception:
        return 0
    for name in z.namelist():
        if not name.endswith('.class'):
            continue
        try:
            d = z.read(name)
        except Exception:
            continue
        if d[:4] != b'\xca\xfe\xba\xbe':
            continue
        try:
            cnt = struct.unpack('>H', d[8:10])[0]
            i = 10
            idx = 1
            while idx < cnt:
                tag = d[i]
                if tag == 1:
                    ln = struct.unpack('>H', d[i+1:i+3])[0]
                    raw = d[i+3:i+3+ln]
                    try:
                        s = raw.decode('utf-8', 'replace')
                    except Exception:
                        s = ''
                    if any('\u4e00' <= c <= '\u9fff' for c in s):
                        n += 1
                    i += 3 + ln
                elif tag in (7, 8, 16, 19, 20):
                    i += 3
                elif tag == 15:
                    i += 4
                elif tag in (3, 4, 9, 10, 11, 12, 17, 18):
                    i += 5
                elif tag in (5, 6):
                    i += 9
                    idx += 1
                else:
                    break
                idx += 1
        except Exception:
            continue
    return n

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(0)
    else:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        print(count(sys.argv[1]))
