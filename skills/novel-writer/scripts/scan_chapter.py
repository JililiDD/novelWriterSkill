#!/usr/bin/env python3
"""
scan_chapter.py — Unified All-in-One Chapter Diagnostic Scanner

Executes a comprehensive single-command scan of candidate fiction prose:
1. Dialogue Fragmentation & Question Chains (FP-001)
2. Explanatory Summaries & Stock Reaction Clichés (FP-004)
3. Paragraph Shape & Cadence Monotony (FP-005)
4. (Optional) Chapter Interface Boundary Extraction

Usage:
    python3 scan_chapter.py <candidate.md>
    python3 scan_chapter.py <candidate.md> --prev <chapter_N-1.md> --next <chapter_N+1.md>
"""

import sys
import os
import argparse
from dialogue_scan import scan_dialogue
from repetition_scan import scan_repetitions
from paragraph_shape_scan import scan_paragraph_shapes
from chapter_interface_scan import extract_paragraphs, print_block

def run_unified_scan(curr_path, prev_path=None, next_path=None):
    if not os.path.exists(curr_path):
        print(f"Error: Target chapter file not found: {curr_path}", file=sys.stderr)
        sys.exit(1)

    print("\n" + "=" * 70)
    print(f"  NOVEL WRITER — UNIFIED CHAPTER DIAGNOSTIC REPORT")
    print(f"  Target File: {os.path.abspath(curr_path)}")
    print("=" * 70)

    # 1. Dialogue Scan
    print("\n" + ">>> 1. DIALOGUE ENGINE & VOICE INTEGRITY SCAN (FP-001)")
    scan_dialogue(curr_path)

    # 2. Repetition & Cliché Scan
    print("\n" + ">>> 2. EXPLANATORY BUDGET & CLICHÉ REPETITION SCAN (FP-004)")
    scan_repetitions(curr_path)

    # 3. Paragraph Shape Scan
    print("\n" + ">>> 3. PARAGRAPH GEOMETRY & RHYTHM VARIATION SCAN (FP-005)")
    scan_paragraph_shapes(curr_path)

    # 4. Optional Interface Boundary Scan
    if prev_path or next_path:
        print("\n" + ">>> 4. CHAPTER INTERFACE CONTINUITY")
        curr_paras = extract_paragraphs(curr_path)
        if prev_path:
            prev_paras = extract_paragraphs(prev_path)
            print_block(f"Chapter N-1 ({os.path.basename(prev_path)})", prev_paras, is_head=False, count=2)
        print_block(f"Chapter N ({os.path.basename(curr_path)})", curr_paras, is_head=True, count=2)
        print_block(f"Chapter N ({os.path.basename(curr_path)})", curr_paras, is_head=False, count=2)
        if next_path:
            next_paras = extract_paragraphs(next_path)
            print_block(f"Chapter N+1 ({os.path.basename(next_path)})", next_paras, is_head=True, count=2)

    print("\n" + "=" * 70)
    print("  DIAGNOSTIC SUMMARY COMPLETE")
    print("=" * 70 + "\n")

def main():
    parser = argparse.ArgumentParser(description="Run complete unified diagnostics on a fiction chapter.")
    parser.add_argument("candidate", help="Path to current chapter candidate (.md)")
    parser.add_argument("--prev", default=None, help="Path to previous chapter (.md)")
    parser.add_argument("--next", default=None, help="Path to next chapter (.md)")

    args = parser.parse_args()
    run_unified_scan(args.candidate, args.prev, args.next)

if __name__ == '__main__':
    main()
