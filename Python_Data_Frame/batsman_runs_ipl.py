import numpy as np
import pandas as pd

# Load the dataset
context = pd.read_csv('C:/Users/samar/Downloads/batsman_runs_ipl.csv')

# Display the dataset
print(context)

# Check the type of context
print(type(context))

# Display the first two rows
print(context.head(2))

# Rename columns
context = context.rename(columns={'batter': 'batsman'})
print(context)

# Accessing Single Row
single_batter = context[context.batsman == 'A Ashish Reddy']
print(single_batter)

# Accessing Single Column
single_column = context['batsman_run']
print(single_column)

# Accessing Multiple Columns
mul_col = context[['batsman', 'batsman_run']]
print(mul_col)

# Using loc for data location
print(context.loc[2, 'batsman_run'])

# Display the batsman_run of the 1st Row
print(context.loc[0, 'batsman_run'])

# Display data in a Range of Rows
print(context.loc[2:5, ['batsman', 'batsman_run']])

# Display the columns batsman and batsman_run from rows 1 to 4
print(context.loc[1:4, ['batsman', 'batsman_run']])

# Include all cols
print(context.loc[2:5])

# Use of iloc(Index Location)
print(context.iloc[2:7, 1]) 

# iloc doesn't include the last range of the row & column
print(context.iloc[2:7, 0:2])

# Display the columns batsman and batsman_run for rows 0 to 5
print(context.iloc[0:6])

# Replacing the Content
context = context.iloc[2:7, 0:2]
print(context)

# Describe
print(context.describe())
