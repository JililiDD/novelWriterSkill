#!/usr/bin/env python3
"""
paragraph_shape_scan.py — Scan fiction prose for monotonous or templated paragraph shapes.

Checks for:
1. Long runs of ultra-short paragraphs (1-2 sentences separated by blank lines).
2. Unnatural uniformity in paragraph character counts (low standard deviation).
3. Monotonous paragraph rhythm (FP-005).

Usage:
    python3 paragraph_shape_scan.py <file_path>
"""

import sys
import os
import math

def scan_paragraph_shapes(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}", file=sys.stderr)
        sys.exit(1)

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        raw_text = f.read()

    # Split into paragraphs by double newlines or single non-empty lines
    raw_paras = [p.strip() for p in raw_text.split('\n\n') if p.strip()]
    
    # Filter out Markdown headers or metadata tables
    paragraphs = []
    for idx, p in enumerate(raw_paras, start=1):
        if p.startswith('#') or p.startswith('---') or p.startswith('|'):
            continue
        paragraphs.append((idx, p, len(p)))

    if not paragraphs:
        print("No valid prose paragraphs found.")
        sys.exit(0)

    lengths = [p[2] for p in paragraphs]
    total_paras = len(paragraphs)
    avg_len = sum(lengths) / total_paras
    variance = sum((l - avg_len) ** 2 for l in lengths) / total_paras
    std_dev = math.sqrt(variance)

    # Detect ultra-short paragraph chains (< 35 characters per paragraph for 4+ consecutive paragraphs)
    short_chains = []
    current_chain = []
    for idx, text, length in paragraphs:
        if length <= 35:
            current_chain.append((idx, text, length))
        else:
            if len(current_chain) >= 4:
                short_chains.append(list(current_chain))
            current_chain = []
    if len(current_chain) >= 4:
        short_chains.append(list(current_chain))

    print(f"=== Paragraph Shape & Rhythm Report: {os.path.basename(file_path)} ===")
    print(f"Total Paragraphs Evaluated: {total_paras}")
    print(f"Average Paragraph Length:   {avg_len:.1f} characters")
    print(f"Length Standard Deviation:  {std_dev:.1f}")
    print("-" * 50)

    print(f"\n[1] Ultra-Short Paragraph Chains (4+ consecutive short paragraphs) — Found: {len(short_chains)}")
    if short_chains:
        for chain in short_chains[:5]:
            start_p = chain[0][0]
            end_p = chain[-1][0]
            print(f"  • Paragraphs {start_p} to {end_p} (Count: {len(chain)}):")
            for p_num, p_text, p_len in chain[:3]:
                print(f"      P{p_num:02d} ({p_len:2d} chars): \"{p_text}\"")
            if len(chain) > 3:
                print(f"      ... and {len(chain) - 3} more short lines")
    else:
        print("  None detected.")

    print("\n[2] Paragraph Length Distribution:")
    buckets = {"1-35 (Short)": 0, "36-100 (Medium)": 0, "101-250 (Long)": 0, "251+ (Heavy)": 0}
    for l in lengths:
        if l <= 35:
            buckets["1-35 (Short)"] += 1
        elif l <= 100:
            buckets["36-100 (Medium)"] += 1
        elif l <= 250:
            buckets["101-250 (Long)"] += 1
        else:
            buckets["251+ (Heavy)"] += 1

    for b_name, count in buckets.items():
        pct = (count / total_paras) * 100
        bar = "█" * int(pct / 5)
        print(f"  {b_name:16s}: {count:3d} ({pct:5.1f}%) {bar}")

    print("-" * 50)
    if len(short_chains) >= 3:
        print("Status: [WARN] Frequent short-paragraph chains detected. Check for fragmented internet-cadence drift.")
    elif std_dev < 20 and total_paras > 10:
        print("Status: [WARN] Abnormally low length variation (std_dev < 20). Check for paragraph geometry monotony.")
    else:
        print("Status: [PASS] Paragraph rhythm variation is healthy.")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 paragraph_shape_scan.py <path_to_markdown_or_txt_file>")
        sys.exit(1)
    scan_paragraph_shapes(sys.argv[1])
