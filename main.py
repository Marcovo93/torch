import sys
import os

def light_my_path(path, format):
    file_found = 0
    if os.path.exists(path):
        if not os.path.isdir(path):
            print("that's not a folder")
        else:
            for roots, dirs, files in os.walk(path):
                for file in files:
                    if file.lower().endswith(format.lower()):
                        full_path = os.path.join(roots, file)
                        file_found += 1
                        print(full_path)

            print(f"file found => {file_found}")
    else:
        print("path not found")


if __name__ == "__main__":
    light_my_path(sys.argv[1], sys.argv[2])