import os, time, sys
import fnmatch
import webbrowser

def find_json_file():
    matches = []
    for root, dirnames, filenames in os.walk(os.getcwd()):
        for filename in fnmatch.filter(filenames, '*.json'):
            matches.append(os.path.join(root, filename))
    return matches

def printf(str):
    print(str)
    sys.stdout.flush()

def findModified(before, after):
    modified = []
    for (bf,bmod) in before.items():
        if (after[bf] and after[bf] > bmod):
            modified.append(bf)
    return modified

def main():
    printf("Watching...")

    before = dict((f, os.path.getmtime(f)) for f in find_json_file())

    while 1:
        time.sleep(1)
        after = dict((f, os.path.getmtime(f)) for f in find_json_file())
        modified = findModified(before,after)
        if modified: 
            os.system("python entertainment_center.py")
            printf("Recompiling... Done!")
            
            # open webbrowser new tab
            url = os.path.abspath('output/index.html')
            webbrowser.open('file://' + url, new=2)

        before = after

if __name__ == '__main__':
    main()
