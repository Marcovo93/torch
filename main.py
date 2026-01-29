import sys; path = sys.argv[1]
from pathlib import Path
import os


p = Path()
file_found = 0


for i in os.listdir(path):
    print(path + "/" + i)
    file_found += 1

print(f"file found {file_found}")