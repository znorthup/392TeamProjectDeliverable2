
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# read csv

df = pd.read_csv('Records.csv')

##########################Part a#############################################
# a. i

# find idex number for the maximum column of Total profit 
max_profit_col = df['Total Profit'].idxmax()
# print other rows based no index number and format them
print('The max profit is: \t ${:,.2f}'.format(df['Total Profit'].loc[max_profit_col]))
print('Found in order #: \t', df['Order ID'].loc[max_profit_col])
print('At index value: \t', max_profit_col)
print()

# a. ii

# find idex number for the minmum column of Total profit 
min_profit_col = df['Total Profit'].idxmin()
# print other rows based no index number and format them
print('The max profit is: \t $', df['Total Profit'].loc[min_profit_col])
print('Found in order #: \t', df['Order ID'].loc[min_profit_col])
print('At index value: \t', min_profit_col)
print()


# a .iii

# sort df based on total profit high to low
df_sorted = df.sort_values(by=['Total Profit'], ascending=False)
# reset the index numebr 
df_sorted = df_sorted.set_index(["Region"]) 
df_sorted = df_sorted.reset_index()

# print title 
print('Top 10 highest total profit items')
print()
print('\t Order ID', '\t', 'Order Date', '\t', 'Total Profit')

# print first 10 item in the df
for i in range(10):
    print('\t', df_sorted['Order ID'].loc[i], '\t', df_sorted['Order Date'].loc[i], '\t', '${:,.2f}'.format(df_sorted['Total Profit'].loc[i]))
    i = 1 + i
# sort df based on total profit low to high
df_sorted = df.sort_values(by=['Total Profit'], ascending=True)
df_sorted = df_sorted.set_index(["Region"]) 
df_sorted = df_sorted.reset_index()

# print title 
print()
print('Top 10 lowest total profit items')
print()
print('\t Order ID', '\t', 'Order Date', '\t', 'Total Profit')

# print first 10 item in the df
for i in range(10):
    print('\t', df_sorted['Order ID'].loc[i], '\t', df_sorted['Order Date'].loc[i], '\t', '${:,.2f}'.format(df_sorted['Total Profit'].loc[i]))
    i = 1 + i
    
##########################Part c##################################

import pickle

# open binary file
df_file = open('record_objects.dat', 'wb')

# set class for read and append
class Df:
    def __init__(self, order_ID, ship_date, total_profit):
        self.__order_ID = order_ID
        self. __ship_date = ship_date
        self.__total_profit = total_profit
    def set_ID(self, ID):
        self.__order_ID = ID
    def set_date(self, date):
        self.__ship_date = date
    def set_profit(self, profit):
        self.__total_profit = profit
    def get_ID(self):
        return self.__order_ID
    def get_date(self):
        return self.__ship_date
    def get_profit(self):
        return self.__total_profit 
    def __str__(self):
        return self.__order_ID 
        return self. __ship_date
        return self.__total_profit



data = Df(df['Order ID'].loc[i], df['Order Date'].loc[i], df['Total Profit'].loc[i])


# set empty list
lis = []
i = 0

# loop to append raw data to list and binary file
for i in range(100):
    # crate new file 
    lis_row = []
    # append data into tempraly list 
    lis_row.append(df['Order ID'].loc[i])
    lis_row.append(df['Order Date'].loc[i])
    lis_row.append(df['Total Profit'].loc[i])
    # append temp list to the list
    lis.append(lis_row)
    i =+ 1

# open file 
df_file = open('record_objects.dat', 'wb')
    
# dump list to the picle 
pickle.dump(lis, df_file)
# close file 
df_file.close()


# open binary file 
df_open = open('record_objects.dat', 'rb')

# assigne open pickle file 
lis_opened = pickle.load(df_open)

# close file
df_open.close()


# print our the 10th data 
print('This is record #10 out of 100:')
print('Order ID:','\t',lis_opened[9][0])
print('Ship Date:','\t',lis_opened[9][1])
print('Total Profit:','\t','${:,.2f}'.format(lis_opened[9][2]))
        
    

