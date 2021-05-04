import pandas as pd

df.to_sql(db_daily_table_name, small_db.con, if_exists='replace', index=False, chunksize=100)