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
                    percorso_completo = os.path.join(roots, file)
                    if format in file:
                        print(percorso_completo)
    else:
        print("path not found")

light_my_path()