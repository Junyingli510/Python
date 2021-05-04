import xlrd, openpyxl

# 1. Read xlsx file
self.input_data = []
INPUT_FILE = 'sam.xlsx'
input_xls = xlrd.open_workbook(INPUT_FILE)
sheet = input_xls.sheet_by_index(0)
for row_index in range(0, sheet.nrows):
    row = [sheet.cell(row_index, col_index).value for col_index in range(sheet.ncols)]
    self.input_data.append(row)


# 2. Write xlsx file
def create_result_file(self):
    self.xfile = openpyxl.load_workbook(self.result_file_name)
    self.sheet = self.xfile.active

    self.row_index = 1


def insert_row(self, result_row):
    self.row_index += 1
    for i, elm in enumerate(result_row):
        self.sheet.cell(row=self.row_index, column=i + 1).value = elm
    self.xfile.save(self.result_file_name)