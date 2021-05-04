import pandas as pd

df["Week"] = pd.to_datetime(df['date']).dt.year.astype(str).str.cat(
            pd.to_datetime(df['date']).dt.week.astype(str).str.zfill(2), sep='-')