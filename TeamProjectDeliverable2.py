
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read csv

df = pd.read_csv('Records.csv')


# a. i

max_profit_col = df['Total Profit'].idxmax()
print('The max profit is: \t ${:,.2f}'.format(df['Total Profit'].loc[max_profit_col]))
print('Found in order #: \t', df['Order ID'].loc[max_profit_col])
print('At index value: \t', max_profit_col)
print()

# a. ii

min_profit_col = df['Total Profit'].idxmin()
print('The max profit is: \t $', df['Total Profit'].loc[min_profit_col])
print('Found in order #: \t', df['Order ID'].loc[min_profit_col])
print('At index value: \t', min_profit_col)
print()


# a .iii

df_sorted = df.sort_values(by=['Total Profit'], ascending=False)
df_sorted = df_sorted.set_index(["Region"]) 
df_sorted = df_sorted.reset_index()
print('Top 10 highest total profit items')
print()
print('\t Order ID', '\t', 'Order Date', '\t', 'Total Profit')


for i in range(10):
    print('\t', df_sorted['Order ID'].loc[i], '\t', df_sorted['Order Date'].loc[i], '\t', '${:,.2f}'.format(df_sorted['Total Profit'].loc[i]))
    i = 1 + i

df_sorted = df.sort_values(by=['Total Profit'], ascending=True)
df_sorted = df_sorted.set_index(["Region"]) 
df_sorted = df_sorted.reset_index()
print()
print('Top 10 lowest total profit items')
print()
print('\t Order ID', '\t', 'Order Date', '\t', 'Total Profit')

for i in range(10):
    print('\t', df_sorted['Order ID'].loc[i], '\t', df_sorted['Order Date'].loc[i], '\t', '${:,.2f}'.format(df_sorted['Total Profit'].loc[i]))
    i = 1 + i
