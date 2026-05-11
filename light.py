import sys
import os
from datetime import datetime

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
    #log management
            tmp_nfl = open('light_my_log','a')
            anno_mese_giorno, ore_minuti = light_my_date()
            tmp_nfl.write('\n')
            tmp_nfl.write('------')
            tmp_nfl.write('\n')
            tmp_nfl.write(f'Log {anno_mese_giorno} at {ore_minuti}')
            tmp_nfl.write('\n')
            tmp_nfl.write('\n')
            i = 0
            for file in file_list:
                i += 1
                tmp_nfl.write(f'{file}\n')
            tmp_nfl.write(f'Total file => {i}')
            tmp_nfl.write('\n')
            tmp_nfl.write('------')
            tmp_nfl.write('\n')
            tmp_nfl.close()
            return file_list
    else:
        raise FileNotFoundError(f"Il percorso {path} non esiste!")


def light_my_date():
    time_now = datetime.now()
    anno_mese_giorno, ora_centesimi = str(time_now).split(' ')
    ore_minuti, centesimi = ora_centesimi.split('.')
    return anno_mese_giorno, ore_minuti