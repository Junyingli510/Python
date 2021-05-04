import requests
import math
import os
from urllib.parse import urlparse

from tqdm import *

def download_zip(self, url):
    print(f"[download_zip] url: {url}")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    }
    r = requests.get(url, stream=True, headers=headers)
    total_length = int(r.headers.get('content-length'))
    zip_fname = os.path.basename(urlparse(r.url).path)

    bar = tqdm(total=math.ceil(total_length / 4096))
    bar.set_description(f"\t{zip_fname} is downloading now...")

    full_zip_fname = os.path.join(self.working_dir, zip_fname)
    with open(full_zip_fname, "wb") as z:
        for chunk in r.iter_content(chunk_size=4096):
            if chunk:
                z.write(chunk)
            bar.update()

    bar.close()

    return full_zip_fname