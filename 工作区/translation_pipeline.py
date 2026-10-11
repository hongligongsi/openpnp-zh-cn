# -*- coding: utf-8 -*-
"""
占位符安全的翻译管线。

约定：
  - 翻译表中用 '§' 代表一个 \x01 占位符
  - 写入前校验：占位符数量、%d/%s/%.Nf 等格式符数量、{} 花括号配对 必须一致
  - 不一致的条目会被拒绝并报告，绝不写入
"""
import re


def ph_count(s):
    return s.count('\x01')


def fmt_tokens(s):
    """提取格式符（%d %s %f %.2f %ld 等），用于一致性校验。
    注意：只针对 % 格式符；花括号内容因可能含占位符，归一化后再比。
    """
    toks = re.findall(r'%[-#0-9.]*[a-zA-Z]', s)
    return sorted(toks)


def brace_shape(s):
    """花括号结构（把 \\x01 与 § 都归一化为 *），用于校验配对与位置"""
    return re.sub(r'[\x01§]', '*', s)


def validate(old, new):
    """返回 (ok, reason)"""
    if '\x01' in new:
        return False, '译文不得直接含 \\x01'
    if new.count('§') != old.count('\x01'):
        return False, f"占位符数量不符: 原 {old.count(chr(1))} vs 译 {new.count('§')}"
    if fmt_tokens(old) != fmt_tokens(new):
        return False, f"格式符不符: {fmt_tokens(old)} vs {fmt_tokens(new)}"
    # 花括号配对数量必须一致
    if old.count('{') != new.count('{') or old.count('}') != new.count('}'):
        return False, f"花括号不符: {old.count('{')}/{old.count('}')} vs {new.count('{')}/{new.count('}')}"
    if not new.strip():
        return False, '译文为空'
    return True, ''


def apply_ph(new):
    return new.replace('§', '\x01')


def build_replacement_map(table, available_strings):
    """table: {原型(带§): 译文(带§)}
    available_strings: 真实字符串集合
    返回 (映射 dict, 报错列表)"""
    # 建索引：原型(§化) -> 真实串
    idx = {}
    for s in available_strings:
        idx.setdefault(s.replace('\x01', '§'), s)

    repl = {}
    errs = []
    for proto, dst in table.items():
        if proto not in idx:
            errs.append(f"[未命中] {proto[:70]}")
            continue
        real = idx[proto]
        ok, why = validate(real, dst)
        if not ok:
            errs.append(f"[校验失败] {proto[:60]} :: {why}")
            continue
        repl[real] = apply_ph(dst)
    return repl, errs
