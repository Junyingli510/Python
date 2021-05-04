import os
import sqlite3 as lite


class DB(object):
    def __init__(self, dst_path, dbname):
        self.DB_Name = dst_path + '/' + dbname
        if not os.path.exists(self.DB_Name):
            open(self.DB_Name, 'w')
        self.setupDBCon()

    def setupDBCon(self):
        self.con = lite.connect(self.DB_Name, check_same_thread=False, isolation_level=None, timeout=20)
        self.cur = self.con.cursor()
        self.cur.execute("PRAGMA synchronous=OFF")
        self.cur.execute('pragma journal_mode=wal')

    def createTable(self, tbl_name, fields):
        # self.dropTable(tbl_name=tbl_name)
        query_fields_list = [f'"{field}" TEXT' for field in fields]
        query_fields = '(' + ", ".join(query_fields_list) + ')'
        final_query = f'CREATE TABLE IF NOT EXISTS {tbl_name} ' + query_fields
        self.cur.execute(final_query)

    def insert_row(self, tbl_name, result_row, start_pos=0, filter_limit=6):
        values = list(result_row.values())
        fields = list(result_row.keys())

        if not self.isExist(tbl_name=tbl_name, condition_row=result_row, filter_limit=filter_limit):
            fields = [f"'{elm}'" for elm in fields]
            query_values = '(' + ', '.join(fields) + ')' + ' VALUES(' + ', '.join([f"'{elm}'" for elm in values]) + ')'
            final_query = f'INSERT OR REPLACE INTO {tbl_name}' + query_values
            self.cur.execute(final_query)
            self.con.commit()

    def select_data(self, tbl_name, condition_row=None, filter_limit=6, start_pos=0):
        query_select = '*'

        if condition_row:
            query_condition = ' WHERE ' + ' AND '.join(
                [f'"{condition_field}"="{condition_value}"' for condition_field, condition_value in
                 zip(list(condition_row.keys())[start_pos:], list(condition_row.values())[:filter_limit])])
        else:
            query_condition = ''

        final_query = 'SELECT ' + query_select + f' FROM {tbl_name}' + query_condition
        self.cur.execute(final_query)
        return self.cur.fetchall()

    def isExist(self, tbl_name, condition_row, filter_limit=6, start_pos=0):
        if self.select_data(tbl_name, condition_row, filter_limit, start_pos):
            return True
        else:
            return False

    def delete(self, tbl_name):
        final_query = f"DELETE FROM {tbl_name} WHERE email NOT LIKE '%@%'"
        self.cur.execute(final_query)
        self.con.commit()

    def dropTable(self, tbl_name):
        final_query = f"DROP TABLE IF EXISTS {tbl_name}"
        self.cur.execute(final_query)

    def closeDB(self):
        self.cur.close()
