import sys
import os
from datetime import datetime

def light_my_path(path, extension):
    file_list = []
    yy_mm_dd, hour_minutes = date_hour()
    log_file = open('light_my_log','a')
    if os.path.exists(path):
        if os.path.isdir(path):
            log_file.write('------')
            log_file.write('\n')
            log_file.write(f'Log {yy_mm_dd} - {hour_minutes}')
            log_file.write('\n')
            log_file.write('\n')
            for roots, dirs, files in os.walk(path):
                for file in files:
                    if file.lower().endswith(extension.lower()):
                        full_path = os.path.join(roots, file)
                        file_list.append(file.lower())
                        log_file.write(file+'\n')
                        print(full_path)
            len_list = len(file_list)
            log_file.write('\n')
            log_file.write(f'Path: {path}\n')
            log_file.write(f'Extension => {extension}\n')
            log_file.write(f'Total file found => {len_list}')
            log_file.write('\n')
            log_file.write('------')
            log_file.close()
            return file_list
        else:
            log_file.write('------')
            log_file.write('\n')
            log_file.write(f'Log {yy_mm_dd} - {hour_minutes}')
            log_file.write('\n')
            log_file.write('\n')
            log_file.write(f"FileNotFoundError: The path {path} is not a folder")
            log_file.write('\n')
            log_file.write('------')
            log_file.close()
            raise FileNotFoundError(f"The path {path} is not a folder")
    else:
        log_file.write('------')
        log_file.write('\n')
        log_file.write(f'Log {yy_mm_dd} - {hour_minutes}')
        log_file.write('\n')
        log_file.write('\n')
        log_file.write(f"FileNotFoundError: The path {path} doesn't exist!")
        log_file.write('\n')
        log_file.write('------')
        log_file.close()
        raise FileNotFoundError(f"The path {path} doesn't exist!")

def log_file(file):
    tmp_nfl = open('light_my_log','a')
    tmp_nfl.write(file+'\n')


def date_hour():
    time_now = datetime.now()
    yy_mm_dd, hour_cent = str(time_now).split(' ')
    hour_minutes, cent = hour_cent.split('.')
    return yy_mm_dd, hour_minutes