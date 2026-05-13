import sys
import os
from datetime import datetime

def light_my_path(path, extension):
    file_list = []
    if os.path.exists(path):
        if os.path.isdir(path):
            yy_mm_dd, hour_minutes = date_hour()
            tmp_nfl = open('light_my_log','a')
            tmp_nfl.write('------')
            tmp_nfl.write('\n')
            tmp_nfl.write(f'Log {yy_mm_dd} - {hour_minutes}')
            tmp_nfl.write('\n')
            tmp_nfl.write('\n')
            for roots, dirs, files in os.walk(path):
                for file in files:
                    if file.lower().endswith(extension.lower()):
                        full_path = os.path.join(roots, file)
                        file_list.append(file.lower())
                        tmp_nfl.write(file+'\n')
                        print(full_path)
            len_list = len(file_list)
            tmp_nfl.write(f'Total file found => {len_list}')
            tmp_nfl.write('\n')
            tmp_nfl.write('------')
            tmp_nfl.close()
            return file_list
        else:
            raise FileNotFoundError(f"Il percorso {path} non è una cartella")
    else:
        raise FileNotFoundError(f"Il percorso {path} non esiste!")

def log_file(file):
    tmp_nfl = open('light_my_log','a')
    tmp_nfl.write(file+'\n')


def date_hour():
    time_now = datetime.now()
    yy_mm_dd, hour_cent = str(time_now).split(' ')
    hour_minutes, cent = hour_cent.split('.')
    return yy_mm_dd, hour_minutes