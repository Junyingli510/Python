import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sales_dict = {'colour': ['Yellow', 'Black', 'Blue', 'Red', 'Yellow', 'Black', 'Blue',
                         'Red', 'Yellow', 'Black', 'Blue', 'Red', 'Yellow', 'Black', 'Blue', 'Red', 'Blue', 'Red'],
              'sales': [100000, 150000, 80000, 90000, 200000, 145000, 120000,
                        300000, 250000, 200000, 160000, 90000, 90100, 150000, 142000, 130000, 400000, 350000],
              'transactions': [100, 150, 820, 920, 230, 120, 70, 250, 250, 110, 130, 860, 980, 300, 150, 170, 230, 280],
              'product': ['type A', 'type A', 'type A', 'type A', 'type A', 'type A', 'type A',
                          'type A', 'type A', 'type B', 'type B', 'type B', 'type B', 'type B', 'type B', 'type B',
                          'type B', 'type B']}

data_sales = pd.DataFrame(sales_dict)
# print(data_sales)

ref_data = data_sales[data_sales.colour == 'Blue'][['sales', 'product']]
ref_data = ref_data.rename(columns={"sales": "sales_1"})

def make_color(d, ref_data):
    # d['sales_2'] = d['sales'] - 1
    d = d.merge(ref_data, how='inner', on='product')
    return d

data_colour = data_sales.groupby('colour').apply(lambda x: make_color(x, ref_data))
print(data_colour)
