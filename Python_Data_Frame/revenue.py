import numpy as np
import pandas as pd
revenue = pd.read_csv('C:/Users/samar/Downloads/revenue-profit.csv')
print(revenue)
revenue = pd.read_csv('C:/Users/samar/Downloads/revenue-profit.csv', sep=';')
print(revenue)
print(type(revenue))
print(revenue.head(2))

#Head
revenue = revenue.rename(columns={'no_data': 'year'})
print(revenue.head(2))

#Accessing Single Row
single_year = revenue[revenue.year == 2012]
print(single_year)

#Accessing Single Column
single_column = revenue['Revenue']
print(single_column)

#Accessing Multiple Columns
mul_col = revenue[['Revenue', 'Profit']]
print(mul_col)

#Using loc in data
print(revenue.loc[2, 'Revenue'])

#Display the profit of 1st Row
print(revenue.loc[0, 'Profit'])

#Display data in a Range of Rows
print(revenue.loc[2:5, ['Revenue', 'Profit']])

#Display the column Year,Revenue and Profit from 1 to 4
print(revenue.loc[1:4, ['year', 'Revenue', 'Profit']])

#Include all cols
print(revenue.loc[2:5])

#Use of iloc(Index Location)
print(revenue.iloc[2:7, 2])  # 2 is the column number

#iloc doesn't include the last range of the row & column
print(revenue.iloc[2:7, 0:3])

#Display the cols years,Revenue,Profit for rows 0 to 5
print(revenue.iloc[0:6])

#Replacing the Content
revenue = revenue.iloc[2:7, 0:4]
print(revenue)

#Describe
print(revenue.describe())
