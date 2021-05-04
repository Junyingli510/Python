import multiprocessing as mp
from time import time
import pandas as pd
import pyreadstat
from multiprocessing import freeze_support

if __name__ == '__main__':
    start_ts = time()
    # df_spss, meta = pyreadstat.read_sav("Surgery.sav", user_missing=False)
    df_spss, meta = pyreadstat.read_file_multiprocessing(pyreadstat.read_sav, "Surgery.sav")

    elapsed_ts = time() - start_ts
    print(elapsed_ts)

