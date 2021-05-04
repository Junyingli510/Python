import os
import fnmatch
import json
import shutil
import time
total_cnt = 0

PATH = ''
for path, dirs, files in os.walk(PATH):
    for f in fnmatch.filter(files, 'meta'):
        fullname = os.path.abspath(os.path.join(path, f))
        json_info = eval(open(fullname, "r").read())
        status = json_info['status']
        response_url = json_info['response_url']
        total_cnt += 1

        if status in [307, 403, 407, 504, 520, 522, 524, 525]:
            shutil.rmtree(path)
            print(status, path)
