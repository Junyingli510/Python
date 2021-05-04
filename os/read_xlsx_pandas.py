import pandas as pd

df = pd.read_excel('ExampleRename.xlsx', sheetname='Sheet1')

org_name_list = list(df['Original Name'])
rename_list = list(df['New Name'])

for org_name, new_name in zip(org_name_list, rename_list):
    print(org_name, new_name)

