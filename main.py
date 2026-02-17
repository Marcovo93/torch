import sys
import os
import glob

def light_my_path(path = sys.argv[1], format = sys.argv[2]):
    file_found = 0
    if os.path.exists(path):
        if not os.path.isdir(path):
            print("that's not a folder")
        else:
            file_count = 0
            file = glob.glob(f"{path}/**/*.{format}", recursive=True, include_hidden=True)
            for p in file:
                file_count += 1
                print(p)
            print(file_count)
    else:
        print("path not found")

light_my_path()