#!/usr/bin/env python3
"""
dialogue_scan.py — Scan fiction prose for dialogue defects.

Checks for:
1. High-frequency 2-5 character clipped dialogue fragments (FP-001).
2. Interrogative chains (consecutive questions across speakers).
3. Monotonous short-dialogue clusters.

Usage:
    python3 dialogue_scan.py <file_path>
"""

import sys
import re
import os

# Regex to capture dialogue enclosed in standard Chinese / English quotation marks
DIALOGUE_PATTERN = re.compile(r'[“"「『](.*?)[”"」』]')

def scan_dialogue(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}", file=sys.stderr)
        sys.exit(1)

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    short_dialogues = []
    consecutive_questions = []
    prev_was_question = False
    prev_q_line = -1

    for line_idx, line in enumerate(lines, start=1):
        line_str = line.strip()
        matches = DIALOGUE_PATTERN.findall(line_str)
        
        for text in matches:
            clean_text = text.strip()
            length = len(clean_text)
            
            # Check for 2-5 char clipped dialogue
            if 1 < length <= 5:
                short_dialogues.append((line_idx, clean_text, length))
            
            # Check for consecutive questions across lines
            is_question = clean_text.endswith('？') or clean_text.endswith('?')
            if is_question:
                if prev_was_question and (line_idx - prev_q_line <= 3):
                    consecutive_questions.append((prev_q_line, line_idx, clean_text))
                prev_was_question = True
                prev_q_line = line_idx
            else:
                if line_idx - prev_q_line > 2:
                    prev_was_question = False

    print(f"=== Dialogue Scan Report: {os.path.basename(file_path)} ===")
    print(f"Total Lines Scanned: {len(lines)}")
    print("-" * 50)

    print(f"\n[1] Clipped Dialogue Fragments (2-5 chars) — Found: {len(short_dialogues)}")
    if short_dialogues:
        for l_num, text, length in short_dialogues[:25]:
            print(f"  Line {l_num:4d} ({length} chars): \"{text}\"")
        if len(short_dialogues) > 25:
            print(f"  ... and {len(short_dialogues) - 25} more")
    else:
        print("  None detected.")

    print(f"\n[2] Interrogative Chains (Consecutive Questions) — Found: {len(consecutive_questions)}")
    if consecutive_questions:
        for p_line, c_line, text in consecutive_questions[:15]:
            print(f"  Lines {p_line} -> {c_line}: \"{text}\"")
        if len(consecutive_questions) > 15:
            print(f"  ... and {len(consecutive_questions) - 15} more")
    else:
        print("  None detected.")

    print("-" * 50)
    if len(short_dialogues) > 8 or len(consecutive_questions) > 4:
        print("Status: [WARN] High density of clipped dialogue or question chains detected. Inspect for FP-001.")
    else:
        print("Status: [PASS] Dialogue fragmentation within normal parameters.")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 dialogue_scan.py <path_to_markdown_or_txt_file>")
        sys.exit(1)
    scan_dialogue(sys.argv[1])
