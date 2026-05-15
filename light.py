import os
from datetime import datetime

def light_my_path(path, extension):
    start_cronos()
    file_list = []
    if os.path.exists(path):
        if os.path.isdir(path):
            yy_mm_dd, hour_minutes = date_hour()
            log_file = open(f'Log-{yy_mm_dd}', 'a')
            log_file.write(f'{yy_mm_dd} {hour_minutes}: file *.{extension} search starting...\n')
            for roots, dirs, files in os.walk(path):
                for file in files:
                    if file.lower().endswith(extension.lower()):
                        full_path = os.path.join(roots, file)
                        file_list.append(file.lower())
                        create_log(file)
                        print(full_path)
            delta = cronos()
            log_file.write(f'{yy_mm_dd} {hour_minutes}: process ended with no errors.\n')
            log_file.write(f'Found {len(file_list)} files. it took {delta}ms')
            log_file.close()
            stop_cronos()
            return file_list
        else:
            raise FileNotFoundError(f"The path {path} is not a folder")
    else:
        raise FileNotFoundError(f"The path {path} doesn't exist!")

def create_log(file):
    yy_mm_dd, hour_minutes = date_hour()
    log_file = open(f'Log-{yy_mm_dd}', 'a')
    yy_mm_dd, hour_minutes = date_hour()
    log_file.write(f'{yy_mm_dd} {hour_minutes}: file {file}' + '\n')
    log_file.close()

def date_hour():
    time_now = datetime.now()
    yy_mm_dd, hour_cent = str(time_now).split(' ')
    hour_minutes, cent = hour_cent.split('.')
    return yy_mm_dd, hour_minutes

def start_cronos():
    time_now = datetime.now()
    yy_mm_dd, hour_cent = str(time_now).split(' ')
    hour_minutes, cent = hour_cent.split('.')
    return cent


def stop_cronos():
    time_now = datetime.now()
    yy_mm_dd, hour_cent = str(time_now).split(' ')
    hour_minutes, cent = hour_cent.split('.')
    return cent


def cronos():
    start = int(start_cronos())
    stop = int(stop_cronos())
    delta = stop - start
    return delta
