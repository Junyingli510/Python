import multiprocessing as mp
from time import time

import pandas as pd
import pyreadstat

def worker(inpt):
    import pyreadstat
    offset, chunksize, path = inpt
    df, meta = pyreadstat.read_sav(path, row_offset=offset, row_limit=chunksize)
    return df

# calculate the number of rows in the file
_, meta = pyreadstat.read_sav("big.sav", metadataonly=True)
numrows = meta.number_rows
# calculate number of cores in the machine, this could also be set manually to some number, i.e. 8
numcores = mp.cpu_count()
# calculate the chunksize and offsets
divs = [numrows // numcores + (1 if x < numrows % numcores else 0)  for x in range (numcores) ]
chunksize = divs[0]
offsets = [indx*chunksize for indx in range(numcores)]
# pack the data for the jobs
jobs = [(x, chunksize, "big.sav") for x in offsets]

pool = mp.Pool(processes=numcores)
# let's go!
t0=time()
chunks = pool.map(worker, jobs)
t1=time()
print(t1-t0) # this prints 29 seconds
# chunks is a list of dataframes in the right order
# you can concatenate all the chunks into a single big dataframe if you like
final = pd.concat(chunks, axis=0, ignore_index=True)