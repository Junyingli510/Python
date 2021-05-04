import pandas as pd

writer = pd.ExcelWriter("data.xlsx", engine='xlsxwriter')

df.to_excel(writer, sheet_name='Sheet1', index=False)

# Get the xlsxwriter workbook and worksheet objects.
workbook = writer.book
worksheet = writer.sheets['Sheet1']
