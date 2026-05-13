import os
from datetime import datetime

def light_my_path(path, extension):
    file_list = []
    if os.path.exists(path):
        if os.path.isdir(path):
            for roots, dirs, files in os.walk(path):
                for file in files:
                    if file.lower().endswith(extension.lower()):
                        full_path = os.path.join(roots, file)
                        file_list.append(file.lower())
                        log_file(file)
                        print(full_path)
            return file_list
        else:
            raise FileNotFoundError(f"The path {path} is not a folder")
    else:
        raise FileNotFoundError(f"The path {path} doesn't exist!")

def log_file(file):
    log_file = open('light_my_log','a')
    log_file.write(file + '\n')
    log_file.close()


def date_hour():
    time_now = datetime.now()
    yy_mm_dd, hour_cent = str(time_now).split(' ')
    hour_minutes, cent = hour_cent.split('.')
    return yy_mm_dd, hour_minutes