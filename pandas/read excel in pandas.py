import pandas as pd
import os

df = pd.read_sql_table('temp_new', f"sqlite:///{os.path.join(working_dir, big_db_name)}")