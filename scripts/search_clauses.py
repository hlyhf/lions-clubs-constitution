#!/usr/bin/env python3
"""中国狮子联会基本法 条款检索脚本（lions-cls skill 配套）

用法:
    python3 search_clauses.py <关键词> [文件名子串]

示例:
    python3 search_clauses.py 会费
    python3 search_clauses.py 服务队 工作规则
    python3 search_clauses.py 标识 会员行为准则

说明:
    在 references/ 下的官方文件文本化 Markdown 中检索关键词，
    输出命中行及其所在文件与页码（如可识别），供 Agent 快速定位条款。
"""
import os
import re
import sys

REF_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "references")

FILES = [
    "章程.md",
    "工作规则.md",
    "财务管理制度.md",
    "会费收取办法.md",
    "会员行为准则.md",
    "VI手册A.md",
    "VI手册B.md",
    "templates.md",
]

PAGE_RE = re.compile(r"^##\s*第\s*(\d+)\s*页")
CLAUSE_RE = re.compile(r"第[一二三四五六七八九十百]+条")


def search(keyword: str, file_filter: str = ""):
    hits = 0
    for fname in FILES:
        if file_filter and file_filter not in fname:
            continue
        path = os.path.join(REF_DIR, fname)
        if not os.path.exists(path):
            continue
        page = None
        with open(path, encoding="utf-8") as f:
            for lineno, line in enumerate(f, 1):
                m = PAGE_RE.match(line.strip())
                if m:
                    page = m.group(1)
                if keyword in line:
                    clause = ""
                    cm = CLAUSE_RE.search(line)
                    if cm:
                        clause = cm.group(0)
                    tag = f"第{page}页" if page else "—"
                    print(f"[{fname} | {tag} | L{lineno}]{('[' + clause + ']') if clause else ''} {line.strip()}")
                    hits += 1
    if not hits:
        print(f"未找到“{keyword}”。请尝试其他关键词，或确认关键词与官方文件用语一致。")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    kw = sys.argv[1]
    filt = sys.argv[2] if len(sys.argv) > 2 else ""
    search(kw, filt)
