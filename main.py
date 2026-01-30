import sys; path = sys.argv[1]
from pathlib import Path
import os

dir_found = 0
file_found = 0


if os.path.exists(path):
    if not os.path.isdir(path):
        print("that's not a dir")
    else:
        for i in os.listdir(path):
           print(path + i)
           file_found += 1
        print(f"file found {file_found}")
else:
    print("path not found")

print(os.path.getatime(path))