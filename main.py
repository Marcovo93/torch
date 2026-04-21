import sys
import os

def light_my_path(path = sys.argv[1], format = sys.argv[2]):
    file_found = 0
    if os.path.exists(path):
        if not os.path.isdir(path):
            print("that's not a folder")
        else:
            for roots, dirs, files in os.walk(path):
                for file in files:
                    file_split = file.split(".")
                    if format.lower() in file_split or format.upper() in file_split:
                        percorso_completo = os.path.join(roots, file)
                        file_found += 1
                        print(percorso_completo)

            print(f"file found => {file_found}")
    else:
        print("path not found")

light_my_path()