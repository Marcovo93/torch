import sys; path = sys.argv[1]
from pathlib import Path
import os

def light_my_path():
    dir_found = 0
    file_found = 0


    if os.path.exists(path):
        if not os.path.isdir(path):
            print("that's not a dir")
        else:
            for w in os.walk(path):
               print(w)
               file_found += 1
            print(f"file found {file_found}")
    else:
        print("path not found")


light_my_path()