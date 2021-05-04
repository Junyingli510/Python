def set_format_tipranks_sheet(self, size_dataframe, worksheet, workbook):
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
    worksheet.set_column('U:U', None, cell_format3)

    currency_format = workbook.add_format({'num_format': '$#,##0.00'})
    worksheet.set_column('C:I', None, currency_format)
    worksheet.set_column('L:L', None, currency_format)
    worksheet.set_column('T:T', None, currency_format)

    date_format = workbook.add_format({'num_format': 'yyyy-mm-dd'})
    worksheet.set_column('AJ:AK', None, date_format)
    worksheet.set_column('AM:AM', None, date_format)

    number_format = workbook.add_format({'num_format': '#,##0.00'})
    worksheet.set_column('J:K', None, number_format)
    worksheet.set_column('AI:AI', None, number_format)
    worksheet.set_column('N:N', None, number_format)

    bad_cell_format = workbook.add_format()
    bad_cell_format.set_bg_color(self.color_format['Bad']['bg'])
    bad_cell_format.set_font_color(self.color_format['Bad']['font'])

    good_cell_format = workbook.add_format()
    good_cell_format.set_bg_color(self.color_format['Good']['bg'])
    good_cell_format.set_font_color(self.color_format['Good']['font'])

    neutral_cell_format = workbook.add_format()
    neutral_cell_format.set_bg_color(self.color_format['Neutral']['bg'])
    neutral_cell_format.set_font_color(self.color_format['Neutral']['font'])

    warning_cell_format = workbook.add_format()
    warning_cell_format.set_bg_color(self.color_format['Warning']['bg'])
    warning_cell_format.set_font_color(self.color_format['Warning']['font'])

    accent2_cell_format = workbook.add_format()
    accent2_cell_format.set_bg_color(self.color_format['Accent2_20%']['bg'])
    accent2_cell_format.set_font_color(self.color_format['Accent2_20%']['font'])

    accent3_cell_format = workbook.add_format()
    accent3_cell_format.set_bg_color(self.color_format['Accent3_20%']['bg'])
    accent3_cell_format.set_font_color(self.color_format['Accent3_20%']['font'])

    green_cell_format = workbook.add_format()
    green_cell_format.set_font_color('#00FF00')

    red_cell_format = workbook.add_format()
    red_cell_format.set_font_color('#FF0000')

    black_cell_format = workbook.add_format()
    black_cell_format.set_font_color('#000000')

    five_level_cell_format_list = [
        good_cell_format, accent3_cell_format, warning_cell_format, accent2_cell_format, bad_cell_format
    ]
    for i, five_level_cell_format in enumerate(five_level_cell_format_list):
        worksheet.conditional_format(f'O2:O{size_dataframe}', {'type': 'cell',
                                                               'criteria': '==',
                                                               'value': i + 1,
                                                               'format': five_level_cell_format})

    worksheet.conditional_format(f'T2:T{size_dataframe}', {'type': 'formula',
                                                           'criteria': '=$U2>0',
                                                           'format': green_cell_format,
                                                           })
    worksheet.conditional_format(f'T2:T{size_dataframe}', {'type': 'formula',
                                                           'criteria': '=$U2<0',
                                                           'format': red_cell_format,
                                                           })
    worksheet.conditional_format(f'T2:T{size_dataframe}', {'type': 'formula',
                                                           'criteria': '=$U2="N/A"',
                                                           'format': black_cell_format,
                                                           })

    worksheet.conditional_format(f'U2:U{size_dataframe}', {'type': 'cell',
                                                           'criteria': '>',
                                                           'value': 0,
                                                           'format': green_cell_format})
    worksheet.conditional_format(f'U2:U{size_dataframe}', {'type': 'cell',
                                                           'criteria': '<',
                                                           'value': 0,
                                                           'format': red_cell_format})
    worksheet.conditional_format(f'U2:U{size_dataframe}', {'type': 'cell',
                                                           'criteria': '==',
                                                           'value': '"N/A"',
                                                           'format': black_cell_format})

    green_cell_format = workbook.add_format()
    green_cell_format.set_font_color('#00FF00')

    red_cell_format = workbook.add_format()
    red_cell_format.set_font_color('#FF0000')

    black_cell_format = workbook.add_format()
    black_cell_format.set_font_color('#000000')

    gray_cell_format = workbook.add_format()
    gray_cell_format.set_font_color('#808080')

    smart_color_list = [
        "#C00004", "#F08C8E", "#F3A3A5", "#EECD94", "#E9D686", "#E9DE85", "#E4DE85", "#C8E0A0", "#BAD988", "#AFCC80"
    ]

    for i, smart_color in enumerate(smart_color_list):
        smart_cell_format = workbook.add_format()
        smart_cell_format.set_font_color(smart_color)

        worksheet.conditional_format(f'V2:V{size_dataframe}', {'type': 'cell',
                                                               'criteria': '==',
                                                               'value': i + 1,
                                                               'format': smart_cell_format})

    worksheet.conditional_format(f'W2:W{size_dataframe}', {'type': 'cell',
                                                           'criteria': '==',
                                                           'value': '"Bullish"',
                                                           'format': green_cell_format})
    worksheet.conditional_format(f'W2:W{size_dataframe}', {'type': 'cell',
                                                           'criteria': '==',
                                                           'value': '"Bearish"',
                                                           'format': red_cell_format})
    worksheet.conditional_format(f'W2:W{size_dataframe}', {'type': 'formula',
                                                           'criteria': 'AND($W2<> "Bullish", $W2 <>"Bearish")',
                                                           'format': gray_cell_format})

    worksheet.conditional_format(f'X2:X{size_dataframe}', {'type': 'cell',
                                                           'criteria': '==',
                                                           'value': '"Increased"',
                                                           'format': green_cell_format})
    worksheet.conditional_format(f'X2:X{size_dataframe}', {'type': 'cell',
                                                           'criteria': '==',
                                                           'value': '"Decreased"',
                                                           'format': red_cell_format})
    worksheet.conditional_format(f'X2:X{size_dataframe}', {'type': 'formula',
                                                           'criteria': 'AND($W2<> "Increased", $W2 <>"Decreased")',
                                                           'format': gray_cell_format})

    worksheet.conditional_format(f'Y2:Y{size_dataframe}', {'type': 'cell',
                                                           'criteria': '==',
                                                           'value': '"Bought Shares"',
                                                           'format': green_cell_format})
    worksheet.conditional_format(f'Y2:Y{size_dataframe}', {'type': 'cell',
                                                           'criteria': '==',
                                                           'value': '"Sold Shares"',
                                                           'format': red_cell_format})
    worksheet.conditional_format(f'Y2:Y{size_dataframe}', {'type': 'formula',
                                                           'criteria': 'AND($W2<> "Bought Shares", $W2 <>"Sold Shares")',
                                                           'format': gray_cell_format})

    tipranks_investors_list = [
        '"Very Positive"', '"Positive"', '"Neutral"', '"Negative"', '"Very Negative"'
    ]

    for i, five_level_cell_format in enumerate(five_level_cell_format_list):
        worksheet.conditional_format(f'Z2:Z{size_dataframe}', {'type': 'cell',
                                                               'criteria': '==',
                                                               'value': tipranks_investors_list[i],
                                                               'format': five_level_cell_format})

    news_sentiment_list = [
        '"Very Positive"', '"Positive"', '"Neutral"', '"Negative"', '"Very Negative"'
    ]

    for i, five_level_cell_format in enumerate(five_level_cell_format_list):
        worksheet.conditional_format(f'AA2:AA{size_dataframe}', {'type': 'cell',
                                                                 'criteria': '==',
                                                                 'value': news_sentiment_list[i],
                                                                 'format': five_level_cell_format})

    worksheet.conditional_format(f'AB2:AB{size_dataframe}', {'type': 'cell',
                                                             'criteria': '==',
                                                             'value': '"Positive"',
                                                             'format': green_cell_format})
    worksheet.conditional_format(f'AB2:AB{size_dataframe}', {'type': 'cell',
                                                             'criteria': '==',
                                                             'value': '"Negative"',
                                                             'format': red_cell_format})
    worksheet.conditional_format(f'AB2:AB{size_dataframe}', {'type': 'formula',
                                                             'criteria': 'AND($W2<> "Positive", $W2 <>"Negative")',
                                                             'format': gray_cell_format})

    worksheet.conditional_format(f'AC2:AC{size_dataframe}', {'type': 'cell',
                                                             'criteria': '>',
                                                             'value': 0,
                                                             'format': green_cell_format})
    worksheet.conditional_format(f'AC2:AC{size_dataframe}', {'type': 'cell',
                                                             'criteria': '<',
                                                             'value': 0,
                                                             'format': red_cell_format})
    worksheet.conditional_format(f'AC2:AC{size_dataframe}', {'type': 'cell',
                                                             'criteria': '==',
                                                             'value': '"N/A"',
                                                             'format': black_cell_format})

    worksheet.conditional_format(f'AD2:AD{size_dataframe}', {'type': 'cell',
                                                             'criteria': '>',
                                                             'value': 0,
                                                             'format': green_cell_format})
    worksheet.conditional_format(f'AD2:AD{size_dataframe}', {'type': 'cell',
                                                             'criteria': '<',
                                                             'value': 0,
                                                             'format': red_cell_format})
    worksheet.conditional_format(f'AD2:AD{size_dataframe}', {'type': 'cell',
                                                             'criteria': '==',
                                                             'value': '"N/A"',
                                                             'format': black_cell_format})
