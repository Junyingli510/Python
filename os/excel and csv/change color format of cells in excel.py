import pandas as pd

data_extracted = {}

df3 = pd.DataFrame(data_extracted)
df3 = df3.fillna('N/A')

writer = pd.ExcelWriter("data.xlsx", engine='xlsxwriter')

df3.to_excel(writer, sheet_name='Sheet1', index=False)

# Get the xlsxwriter workbook and worksheet objects.
workbook = writer.book
worksheet = writer.sheets['Sheet1']

size_dataframe = len(df3.index) + 1

cell_format = workbook.add_format()
cell_format.set_bg_color('#FA8072')
cell_format.set_font_color('#8B0000')

worksheet.conditional_format(f'M2:M{size_dataframe}', {'type': 'cell',
                                                       'criteria': '<=',
                                                       'value': -0.6,
                                                       'format': cell_format})

cell_format2 = workbook.add_format()
cell_format2.set_bg_color('#F79646')
cell_format2.set_font_color('#FFFFFF')
worksheet.conditional_format(f'M2:M{size_dataframe}', {'type': 'cell',
                                                       'criteria': 'between',
                                                       'minimum': -0.3,
                                                       'maximum': -0.6,
                                                       'format': cell_format2})

cell_format5 = workbook.add_format()
cell_format5.set_bg_color('#F0E68C')
cell_format5.set_font_color('#755811')
worksheet.conditional_format(f'M2:M{size_dataframe}', {'type': 'cell',
                                                       'criteria': 'between',
                                                       'minimum': -0.0,
                                                       'maximum': -0.3,
                                                       'format': cell_format5})

cell_format3 = workbook.add_format()
cell_format3.set_num_format('0.00%')
worksheet.set_column('M:M', None, cell_format3)

currency_format = workbook.add_format({'num_format': '$#,##0.00'})
worksheet.set_column('C:I', None, currency_format)
worksheet.set_column('L:L', None, currency_format)

date_format = workbook.add_format({'num_format': 'dd.mm.yyyy'})
worksheet.set_column('R:S', None, date_format)
worksheet.set_column('U:U', None, date_format)

number_format = workbook.add_format({'num_format': '#,##0.00'})
worksheet.set_column('J:K', None, number_format)
worksheet.set_column('O:Q', None, number_format)
worksheet.set_column('V:V', None, number_format)
