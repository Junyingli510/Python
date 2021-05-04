import pandas as pd
from IPython.display import display

dt1 = {
    'aa': ['j', 'b', 'e', 'g', 'i', 'c'],
    "ab": [4, 2, 5, 6, 1, 7],
}

dt2 = {
    'aa': ['b', 'e', 'i', 'j', 'c', 'g'],
    "ac": [4, 9, 5, 8, 3, 4],
}

df1 = pd.DataFrame(dt1)

# df1 = df1.set_index('aa')
display(df1)

df2 = pd.DataFrame(dt2)
# df2 = df2.set_index('aa')
display(df2)

# df3 = pd.concat([df1, df2], axis=1, sort=False)
# df3.reset_index(inplace=True)
# df3 = df3.rename(columns = {'index':'aa'})
# display(df3)

df3 = df1.merge(df2, how='left')
df3 = df3.reindex(sorted(df3.columns), axis=1)

df3 = df3[['ac', 'aa', 'ab']]
display(df3)
