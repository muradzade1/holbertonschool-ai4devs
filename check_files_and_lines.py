#!/usr/bin/env python3
import os
import glob

def main():
    # Mümkün qovluq yollarını yoxla
    possible_paths = [
        "prompting_debug_assistant/bug_snippets",
        "./prompting_debug_assistant/bug_snippets",
        "../prompting_debug_assistant/bug_snippets"
    ]
    
    bug_dir = None
    for path in possible_paths:
        if os.path.exists(path):
            bug_dir = path
            break
    
    if not bug_dir:
        print("ERROR: bug_snippets directory not found")
        return 1
    
    # Faylları tap
    expected_files = ["bug1.py", "bug2.py", "bug3.js", "bug4.js", "bug5.java", "bug6.py", "bug_descriptions.md"]
    found_files = []
    
    for fname in expected_files:
        fpath = os.path.join(bug_dir, fname)
        if os.path.exists(fpath):
            found_files.append(fpath)
    
    if len(found_files) != 7:
        print("ERROR: Expected 7 files, found {}".format(len(found_files)))
        return 1
    
    # Nəticələri göstər
    print("Found {} files:\n".format(len(found_files)))
    for fpath in sorted(found_files):
        fname = os.path.basename(fpath)
        with open(fpath, 'r') as f:
            lines = sum(1 for _ in f)
        print("  {}: {} lines".format(fname, lines))
    
    return 0

if __name__ == "__main__":
    exit(main())
