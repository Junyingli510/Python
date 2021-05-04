import pandas as pd


ips = pd.read_csv('Result1.csv', names=['IP','Domain','Country','Region','City','ISP','ASN'], encoding='ISO-8859-1')
org_file = pd.read_csv('WA_2017_append.csv', names=['First Name', 'Last Name', 'DOB', 'IP'], encoding='ISO-8859-1')

merged_left = pd.merge(left=org_file,right=ips, how='left', left_on='IP', right_on='IP')
merged_left.to_csv('WA_2017_append(result).csv', sep=',', encoding='utf-8', header=True)