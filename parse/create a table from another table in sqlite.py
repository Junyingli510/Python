import sqlite3 as lite

query = f'''CREATE TABLE temp_new AS 
                  SELECT
                  Ticker as stock,
                  Date as date,
                  round(`Adj. Open`,2) as open,
                  round(`Adj. High`,2) as high,
                  round(`Adj. Low`,2) as low,
                  round(`Adj. Close`,2) as close,
                  round(`Adj. Volume`, 2) as volume
                  FROM {self.db_daily_table_name} 
                  WHERE Date>='{first_year}-01-01'
        '''
self.big_db.cur.execute(query)