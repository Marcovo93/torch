import sys
import os

def light_my_path(path, format):
    file_list = []
    if os.path.exists(path):
        if not os.path.isdir(path):
            raise FileNotFoundError(f"Il percorso {path} non è una cartella")
        else:
            for roots, dirs, files in os.walk(path):
                for file in files:
                    if file.lower().endswith(format.lower()):
                        full_path = os.path.join(roots, file)
                        file_list.append(file.lower())
                        print(full_path)

            return file_list
    else:
        raise FileNotFoundError(f"Il percorso {path} non esiste!")
