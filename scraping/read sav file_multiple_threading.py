import multiprocessing as mp
from time import time

import pandas as pd
import pyreadstat
import math
import threading


def worker(inpt):
    print(inpt)
    offset, chunksize, path = inpt
    df, meta = pyreadstat.read_sav(path, row_offset=offset, row_limit=chunksize)
    # df, meta = pyreadstat.read_file_in_chunks(pyreadstat.read_sav, path, offset=offset, chunksize=chunksize,
    #                                           multiprocess=True, num_processes=10)
    return df


start_ts = time()

# calculate the number of rows in the file
_, meta = pyreadstat.read_sav("Surgery.sav", metadataonly=True)
numrows = meta.number_rows
# calculate number of cores in the machine, this could also be set manually to some number, i.e. 8
# calculate the chunksize and offsets
chunksize = 200
offsets = [indx * chunksize for indx in range(math.ceil(numrows / chunksize))]
# pack the data for the jobs
jobs = [(x, chunksize, "Surgery.sav") for x in offsets]

threads = []
max_threads = 30
while threads or jobs:
    for thread in threads:
        if not thread.is_alive():
            threads.remove(thread)

    while len(threads) < max_threads and jobs:
        job = jobs.pop()
        thread = threading.Thread(target=worker, args=(job,))
        thread.start()
        threads.append(thread)

elapsed_ts = time() - start_ts
print(elapsed_ts)
