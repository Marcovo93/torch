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
                    if file.lower().endswith(format.lower()):
                        percorso_completo = os.path.join(roots, file)
                        file_found += 1
                        print(percorso_completo)

            print(f"file found => {file_found}")
    else:
        print("path not found")

light_my_path()