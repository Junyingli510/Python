format1 = workbook.add_format({'bg_color': '#FFC7CE'})
worksheet.conditional_format('B2:B14',
{'type':'formula',
'criteria': '=$C2<10',
'format': format1
})