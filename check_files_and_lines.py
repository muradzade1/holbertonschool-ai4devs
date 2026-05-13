import os
import glob

def main():
    bug_dir = "prompting_debug_assistant/bug_snippets"
    
    try:
        if not os.path.exists(bug_dir):
            print("ERROR: Directory not found")
            return 1
        
        files = []
        for ext in [".py", ".js", ".java", ".md"]:
            files.extend(glob.glob(os.path.join(bug_dir, "*" + ext)))
        
        if not files:
            print("ERROR: No files found")
            return 1
        
        print("Found {} files:\n".format(len(files)))
        for f in sorted(files):
            name = os.path.basename(f)
            with open(f, "r") as fp:
                lines = len(fp.readlines())
            print("  {}: {} lines".format(name, lines))
        
        return 0
    except Exception as e:
        print("ERROR: {}".format(str(e)))
        return 1

if __name__ == "__main__":
    exit(main())
