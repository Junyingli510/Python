import xlrd

input_dt = {}
input_fname = 'Sample.xlsx'
input_xls = xlrd.open_workbook(input_fname)

sheet_names = input_xls.sheet_names()
sheet = input_xls.sheet_by_index(0)

for i, sheet_name in enumerate(sheet_names):
    sheet = input_xls.sheet_by_name(sheet_name)

    if sheet_name not in input_dt:
        input_dt[sheet_name] = []

    input_xls.sheet_by_name(sheet_name)
    for row_index in range(0, sheet.nrows):
        row = [sheet.cell(row_index, col_index).value for col_index in range(sheet.ncols)]
        input_dt[sheet_name].append(row)