# -*- coding: utf-8 -*-
"""
Java .class 常量池 UTF-8 字符串就地替换器。

原理：
  - class 文件 = 魔数 + 版本 + 常量池 + 访问标志 + 字段/方法/属性
  - 常量池中 CONSTANT_Utf8(tag=1) 的结构为: tag(1) + length(2, big-endian) + bytes[length]
  - 只重写这些条目的 bytes 与 length，常量池条目总数不变
  - 所有对常量池的引用都是「索引」，与字节数据无关 → 无需改动
  - Code 属性中的字节码偏移是「相对 code[] 起始」的 → 与常量池无关 → 无需改动
  - 因此：只要保持常量池条目数量不变，替换字符串数据是安全的

唯一注意：class 文件其他位置的 length 字段（如属性长度）不含常量池数据长度，
  因为它们引用的是索引。唯一例外是无属性区，但属性长度本身不随常量池变化。
"""
import struct


def parse_cp(data):
    """解析常量池，返回 [(tag, start, end, info_dict)] 列表。cp 索引从 1 开始。"""
    assert data[:4] == b'\xca\xfe\xba\xbe', 'not a class file'
    n = struct.unpack('>H', data[8:10])[0]
    entries = [None]  # index 0 占位
    i = 10
    idx = 1
    while idx < n:
        tag = data[i]
        start = i
        if tag == 1:  # Utf8
            ln = struct.unpack('>H', data[i + 1:i + 3])[0]
            i += 3 + ln
            entries.append((1, start, i, {'len_off': start + 1, 'data_off': start + 3, 'length': ln}))
        elif tag in (7, 8, 16, 19, 20):  # Class, String, MethodType, Module, Package
            i += 3
            entries.append((tag, start, i, None))
        elif tag == 15:  # MethodHandle
            i += 4
            entries.append((tag, start, i, None))
        elif tag in (3, 4, 9, 10, 11, 12, 17, 18):  # Integer Float Fieldref Methodref IMethodref NameAndType Dynamic InvokeDynamic
            i += 5
            entries.append((tag, start, i, None))
        elif tag in (5, 6):  # Long Double 占两个槽位
            i += 9
            entries.append((tag, start, i, None))
            entries.append(('reserved', start, i, None))
            idx += 1
        else:
            raise ValueError('unknown cp tag %d at idx %d' % (tag, idx))
        idx += 1
    return entries, i


def get_utf8(data, entries):
    """返回 {字符串: [cp索引...]}"""
    out = {}
    for idx in range(1, len(entries)):
        e = entries[idx]
        if e is None or e[0] != 1:
            continue
        info = e[3]
        b = data[info['data_off']: info['data_off'] + info['length']]
        try:
            s = b.decode('utf-8')
        except Exception:
            continue
        out.setdefault(s, []).append(idx)
    return out


def rebuild(data, replacements):
    """replacements: {旧字符串: 新字符串}（utf-8 字节级）
    返回新的 class 字节。保持常量池条目数不变。"""
    entries, cp_end = parse_cp(data)
    # 逐索引计算新数据
    chunks = []          # 按顺序拼接：cp 之前 + 每个 cp 条目(可能被替换) + cp 之后
    chunks.append(data[:10])
    rep_bytes = {k.encode('utf-8'): v.encode('utf-8') for k, v in replacements.items()}
    hit = 0
    for idx in range(1, len(entries)):
        e = entries[idx]
        if e is None:
            continue
        tag, start, end, info = e
        if tag == 1:
            b = data[info['data_off']: info['data_off'] + info['length']]
            nb = rep_bytes.get(b)
            if nb is not None:
                hit += 1
                if len(nb) > 0xFFFF:
                    raise ValueError('replacement too long (>65535 utf8 bytes)')
                chunks.append(bytes([1]) + struct.pack('>H', len(nb)) + nb)
                continue
        if tag == 'reserved':
            continue  # 已在 Long/Double 内
        chunks.append(data[start:end] if tag != 'reserved' else b'')
    chunks.append(data[cp_end:])
    return b''.join(chunks), hit


if __name__ == '__main__':
    import sys
    print('module')
