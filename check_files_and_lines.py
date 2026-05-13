import os
import sys
import glob

def main():
    bug_dir = "prompting_debug_assistant/bug_snippets"
    
    # Debug məlumatları (stderr-ə yazılır)
    sys.stderr.write("DEBUG: Looking for directory: " + bug_dir + "\n")
    sys.stderr.write("DEBUG: Current working dir: " + os.getcwd() + "\n")
    
    if not os.path.exists(bug_dir):
        sys.stderr.write("ERROR: Directory '" + bug_dir + "' not found!\n")
        return 1
    
    sys.stderr.write("DEBUG: Directory exists at " + os.path.abspath(bug_dir) + "\n")
    
    # Bütün faylları tap
    all_files = []
    
    # Python faylları
    py_files = glob.glob(os.path.join(bug_dir, "*.py"))
    all_files.extend(py_files)
    sys.stderr.write("DEBUG: Found " + str(len(py_files)) + " .py files\n")
    
    # JavaScript faylları
    js_files = glob.glob(os.path.join(bug_dir, "*.js"))
    all_files.extend(js_files)
    sys.stderr.write("DEBUG: Found " + str(len(js_files)) + " .js files\n")
    
    # Java faylları
    java_files = glob.glob(os.path.join(bug_dir, "*.java"))
    all_files.extend(java_files)
    sys.stderr.write("DEBUG: Found " + str(len(java_files)) + " .java files\n")
    
    # Markdown faylları
    md_files = glob.glob(os.path.join(bug_dir, "*.md"))
    all_files.extend(md_files)
    sys.stderr.write("DEBUG: Found " + str(len(md_files)) + " .md files\n")
    
    if not all_files:
        sys.stderr.write("ERROR: No files found in '" + bug_dir + "'!\n")
        return 1
    
    # Nəticələri göstər (stdout-a yazılır)
    print("Found " + str(len(all_files)) + " files:\n")
    for file_path in sorted(all_files):
        filename = os.path.basename(file_path)
        try:
            with open(file_path, 'r') as f:
                lines = sum(1 for _ in f)
            print("  " + filename + ": " + str(lines) + " lines")
        except Exception as e:
            print("  " + filename + ": ERROR - " + str(e))
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
