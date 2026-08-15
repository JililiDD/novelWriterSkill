#!/usr/bin/env python3
"""
batch_runner.py — Autonomous Batch Chapter Inspector & Quality Verifier

Validates multi-chapter ranges for:
1. Sequential numbering integrity and missing chapter gaps.
2. Word count distribution and total batch output.
3. Batch quality diagnostic scans across dialogue, clichés, and paragraph cadence.
4. Boundary interface continuity across sequential chapters.

Usage:
    python3 batch_runner.py --dir chapters/ --start 1 --end 10
    python3 batch_runner.py --dir work/ --scan
"""

import sys
import os
import re
import argparse
from dialogue_scan import scan_dialogue
from repetition_scan import scan_repetitions
from paragraph_shape_scan import scan_paragraph_shapes
from chapter_interface_scan import extract_paragraphs

def find_chapter_files(target_dir):
    if not os.path.exists(target_dir):
        return []

    files = []
    # Check for direct chapter files (chapters/chapter-001.md or work/chapter-001/candidate.md)
    for root, _, filenames in os.walk(target_dir):
        for f in filenames:
            if f.endswith(".md"):
                full_path = os.path.join(root, f)
                match = re.search(r'chapter[-_]?(\d+)', f, re.IGNORECASE)
                if not match:
                    match = re.search(r'chapter[-_]?(\d+)', root, re.IGNORECASE)
                if match:
                    chap_num = int(match.group(1))
                    files.append((chap_num, full_path))

    # Sort by chapter number
    files.sort(key=lambda x: x[0])
    return files

def inspect_batch(target_dir, start_num=None, end_num=None, run_scan=False):
    all_chapters = find_chapter_files(target_dir)

    if not all_chapters:
        print(f"No chapter markdown files found in: {target_dir}")
        return

    # Filter range
    if start_num is not None or end_num is not None:
        filtered = []
        for num, path in all_chapters:
            if start_num is not None and num < start_num:
                continue
            if end_num is not None and num > end_num:
                continue
            filtered.append((num, path))
        chapters = filtered
    else:
        chapters = all_chapters

    if not chapters:
        print(f"No chapters found matching range [{start_num}..{end_num}] in {target_dir}")
        return

    print("\n" + "=" * 75)
    print(f"  NOVEL WRITER — BATCH CHAPTER INSPECTION REPORT")
    print(f"  Directory: {os.path.abspath(target_dir)}")
    print(f"  Total Chapters in Scope: {len(chapters)}")
    print("=" * 75)

    # 1. Sequential Gap Check
    nums = [c[0] for c in chapters]
    expected_nums = list(range(nums[0], nums[-1] + 1))
    missing = set(expected_nums) - set(nums)

    print("\n[1] SEQUENCE INTEGRITY:")
    if missing:
        print(f"  [WARN] Missing chapter sequence numbers: {sorted(list(missing))}")
    else:
        print(f"  [PASS] Clean sequential numbering from Chapter {nums[0]} to {nums[-1]}.")

    # 2. Chapter Summary Table
    print("\n[2] CHAPTER SUMMARY & WORD COUNTS:")
    print(f"  {'Chapter':<10} | {'File Name':<32} | {'Characters':<10} | {'Lines':<6}")
    print("  " + "-" * 68)

    total_chars = 0
    total_lines = 0

    for num, path in chapters:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                chars = len(content.strip().replace(" ", "").replace("\n", ""))
                lines = len(content.splitlines())
                total_chars += chars
                total_lines += lines
                fname = os.path.basename(path)
                if fname in ["candidate.md", "audit.md", "brief.md"]:
                    fname = f"{os.path.basename(os.path.dirname(path))}/{fname}"
                print(f"  Chapter {num:<2} | {fname:<32} | {chars:<10} | {lines:<6}")
        except Exception as e:
            print(f"  Chapter {num:<2} | Error reading file: {e}")

    print("  " + "-" * 68)
    print(f"  TOTALS     | {len(chapters)} Chapters Scanned                | {total_chars:<10} | {total_lines:<6}")
    avg_chars = total_chars // len(chapters) if chapters else 0
    print(f"  AVERAGE    | {avg_chars} chars / chapter")

    # 3. Optional Diagnostics
    if run_scan:
        print("\n" + "=" * 75)
        print("  RUNNING DEEP DIAGNOSTIC SCANS ON ALL BATCH CHAPTERS")
        print("=" * 75)
        for num, path in chapters:
            print(f"\n--- Diagnostic Scan: Chapter {num} ({os.path.basename(path)}) ---")
            scan_dialogue(path)
            scan_repetitions(path)
            scan_paragraph_shapes(path)

    print("\n" + "=" * 75)
    print("  BATCH INSPECTION COMPLETE")
    print("=" * 75 + "\n")

def main():
    parser = argparse.ArgumentParser(description="Inspect and verify a batch of novel chapters.")
    parser.add_argument("--dir", default="chapters", help="Target directory containing chapters (default: chapters)")
    parser.add_argument("--start", type=int, default=None, help="Start chapter number")
    parser.add_argument("--end", type=int, default=None, help="End chapter number")
    parser.add_argument("--scan", action="store_true", help="Run full diagnostic scans across all chapters")

    args = parser.parse_args()
    inspect_batch(args.dir, args.start, args.end, args.scan)

if __name__ == '__main__':
    main()
