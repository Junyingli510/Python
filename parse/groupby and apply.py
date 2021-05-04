import pandas as pd

def make_weekly(d):
    return pd.Series({
        'Open': d["open"].iloc[0],
        'High': d["volume"].max(),
        'Low': d["volume"].min(),
        'Close': d["close"].iloc[d["open"].count() - 1],
        'Volume': d["volume"].sum(),
    })

    # df1 = df.groupby(df["Date"].index.week).apply(make_weekly)


df["Week"] = pd.to_datetime(df['date']).dt.year.astype(str).str.cat(
    pd.to_datetime(df['date']).dt.week.astype(str).str.zfill(2), sep='-')
# display(df)

df1 = df.groupby(['stock', 'Week']).apply(make_weekly)