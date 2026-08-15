#!/usr/bin/env python3
"""
chapter_interface_scan.py — Extract and inspect boundary paragraphs between Chapter N-1, N, and N+1.

Usage:
    python3 chapter_interface_scan.py --curr <chapter_N.md> [--prev <chapter_N-1.md>] [--next <chapter_N+1.md>] [--paras 3]
"""

import sys
import os
import argparse

def extract_paragraphs(file_path):
    if not file_path or not os.path.exists(file_path):
        return []
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        raw = f.read()
    raw_paras = [p.strip() for p in raw.split('\n\n') if p.strip()]
    cleaned = []
    for p in raw_paras:
        if p.startswith('#') or p.startswith('---') or p.startswith('|'):
            continue
        cleaned.append(p)
    return cleaned

def print_block(title, paras, is_head=True, count=3):
    print(f"\n--- {title} ({'Opening' if is_head else 'Ending'} {min(count, len(paras))} Paragraphs) ---")
    if not paras:
        print("  [No data / File not provided]")
        return
    
    selected = paras[:count] if is_head else paras[-count:]
    for idx, p in enumerate(selected, start=1 if is_head else (len(paras) - len(selected) + 1)):
        preview = p if len(p) <= 120 else p[:120] + "..."
        print(f"  [{idx:02d}] {preview}")

def main():
    parser = argparse.ArgumentParser(description="Extract chapter interface boundaries for continuity checking.")
    parser.add_argument("--curr", required=True, help="Path to current chapter (Chapter N)")
    parser.add_argument("--prev", default=None, help="Path to previous chapter (Chapter N-1)")
    parser.add_argument("--next", default=None, help="Path to next chapter (Chapter N+1)")
    parser.add_argument("--paras", type=int, default=3, help="Number of paragraphs to extract at each boundary (default: 3)")

    args = parser.parse_args()

    curr_paras = extract_paragraphs(args.curr)
    prev_paras = extract_paragraphs(args.prev) if args.prev else []
    next_paras = extract_paragraphs(args.next) if args.next else []

    print("=" * 65)
    print(f" CHAPTER INTERFACE INSPECTION REPORT")
    print(f" Current Chapter (N):   {os.path.basename(args.curr)}")
    if args.prev:
        print(f" Previous Chapter (N-1): {os.path.basename(args.prev)}")
    if args.next:
        print(f" Next Chapter (N+1):     {os.path.basename(args.next)}")
    print("=" * 65)

    if prev_paras:
        print_block(f"Chapter N-1 ({os.path.basename(args.prev)})", prev_paras, is_head=False, count=args.paras)
    
    print_block(f"Chapter N ({os.path.basename(args.curr)})", curr_paras, is_head=True, count=args.paras)
    print_block(f"Chapter N ({os.path.basename(args.curr)})", curr_paras, is_head=False, count=args.paras)

    if next_paras:
        print_block(f"Chapter N+1 ({os.path.basename(args.next)})", next_paras, is_head=True, count=args.paras)

    print("\n" + "=" * 65)
    print(" Continuity Checkpoints to Verify Across Boundaries:")
    print("  [ ] 1. Elapsed Time & Time of Day continuity")
    print("  [ ] 2. Physical Location & Room/Spatial continuity")
    print("  [ ] 3. Physical State (injuries, stamina, breath, clothing condition)")
    print("  [ ] 4. Object Custody (items held in hand, packed, or consumed)")
    print("  [ ] 5. Present Characters & Exit/Entrance plausibility")
    print("  [ ] 6. Emotional Aftermath from preceding events")
    print("  [ ] 7. Immediate Objective driving the transition")
    print("=" * 65)

if __name__ == '__main__':
    main()
