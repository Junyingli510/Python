import xlrd

input_dt = []
input_fname = 'excel.xlsx'
input_xls = xlrd.open_workbook(input_fname)
sheet = input_xls.sheet_by_index(0)
for row_index in range(0, sheet.nrows):
    row = [sheet.cell(row_index, col_index).value for col_index in range(sheet.ncols)]
    input_dt.append(row)
