import sys; path = sys.argv[1]
import os

def light_my_path():
    file_found = 0

    if os.path.exists(path):
        if not os.path.isdir(path):
            print("that's not a folder")
        else:
            for roots, dirs, files in os.walk(path):
                print(files)
                file_found += 1
            print(f"file found {file_found}")
    else:
        print("path not found")


light_my_path()
