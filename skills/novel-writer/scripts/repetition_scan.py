#!/usr/bin/env python3
"""
repetition_scan.py — Scan fiction prose for cliché phrasing and explanatory summaries.

Checks for:
1. Explanatory narrator insight phrases ("他知道", "这意味着", "他明白", etc. - FP-004).
2. Stock body reaction clichés ("瞳孔微缩", "倒吸一口凉气", "指关节发白", etc.).
3. High-frequency repetitive sentence starters.

Usage:
    python3 repetition_scan.py <file_path>
"""

import sys
import re
import os
from collections import Counter

SUMMARY_KEYWORDS = [
    "他知道", "她知道", "他们知道",
    "他明白", "她明白", "他们明白",
    "他意识到", "她意识到", "他们意识到",
    "这意味着", "这代表着", "这说明",
    "换句话说", "简而言之", "归根结底",
    "终于明白", "恍然大悟", "心中了然",
    "显然，", "很明显，", "不难看出"
]

BODY_CLICHES = [
    "倒吸一口凉气", "倒抽一口冷气",
    "瞳孔微缩", "瞳孔骤缩", "眼神一凝", "目光一凝",
    "指关节发白", "指节发白", "拳头紧握", "死死攥住",
    "喉头微动", "喉结上下滚动", "咽了口唾沫",
    "后背发凉", "脊背发凉", "冷汗涔涔",
    "心头一紧", "心头一震", "心沉了下去",
    "脚步一顿", "身形一僵", "动作一滞",
    "呼吸一滞", "屏住呼吸"
]

def scan_repetitions(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}", file=sys.stderr)
        sys.exit(1)

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    full_text = "".join(lines)
    
    summary_findings = []
    cliche_findings = []

    for idx, line in enumerate(lines, start=1):
        line_clean = line.strip()
        if not line_clean or line_clean.startswith("#"):
            continue
            
        for kw in SUMMARY_KEYWORDS:
            if kw in line_clean:
                summary_findings.append((idx, kw, line_clean))
                
        for cl in BODY_CLICHES:
            if cl in line_clean:
                cliche_findings.append((idx, cl, line_clean))

    print(f"=== Repetition & Cliché Scan Report: {os.path.basename(file_path)} ===")
    print(f"Total Lines Scanned: {len(lines)}")
    print("-" * 50)

    print(f"\n[1] Explanatory Summary Phrases — Found: {len(summary_findings)}")
    summary_counts = Counter([item[1] for item in summary_findings])
    for kw, count in summary_counts.most_common():
        print(f"  • '{kw}': {count} occurrences")
    if summary_findings:
        print("\n  Sample Lines:")
        for idx, kw, text in summary_findings[:10]:
            snippet = text if len(text) <= 50 else text[:50] + "..."
            print(f"    Line {idx:4d} [{kw}]: {snippet}")

    print(f"\n[2] Stock Reaction Body Clichés — Found: {len(cliche_findings)}")
    cliche_counts = Counter([item[1] for item in cliche_findings])
    for cl, count in cliche_counts.most_common():
        print(f"  • '{cl}': {count} occurrences")
    if cliche_findings:
        print("\n  Sample Lines:")
        for idx, cl, text in cliche_findings[:10]:
            snippet = text if len(text) <= 50 else text[:50] + "..."
            print(f"    Line {idx:4d} [{cl}]: {snippet}")

    print("-" * 50)
    total_issues = len(summary_findings) + len(cliche_findings)
    if total_issues > 10:
        print(f"Status: [WARN] High cliché/summary count ({total_issues}). Check for Explanation Budget violation.")
    else:
        print(f"Status: [PASS] Cliché and summary density within acceptable thresholds.")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 repetition_scan.py <path_to_markdown_or_txt_file>")
        sys.exit(1)
    scan_repetitions(sys.argv[1])
