import numpy as np
import pandas as pd

# Load the dataset
game = pd.read_csv('C:/Users/samar/Practice/Python_Practice/Python_Data_Frame/kohli_ipl.csv')

# Display the dataset
print(game)

# Check the type of game
print(type(game))

# Display the first two rows
print(game.head(2))

# Rename columns
game = game.rename(columns={'match_no': 'match'})
print(game)

# Accessing Single Row
single_row = game[game.match == 2]
print(single_row)

# Accessing Single Column
single_column = game['match']
print(single_column)

# Accessing Multiple Columns
mul_col = game[['match', 'runs']]
print(mul_col)

# Using loc for data location
print(game.loc[2, 'match'])

# Display the match of the 1st Row
print(game.loc[0, 'match'])

# Display data in a Range of Rows
print(game.loc[2:5, ['match', 'runs']])

# Display the columns match and runs from rows 1 to 4
print(game.loc[1:4, ['match', 'runs']])

# Include all cols
print(game.loc[2:5])

# Use of iloc(Index Location)
print(game.iloc[2:7, 1]) 

# iloc doesn't include the last range of the row & column
print(game.iloc[2:7, 0:2])

# Display the columns match and runs for rows 0 to 5
print(game.iloc[0:6])

# Replacing the Content
game = game.iloc[2:7, 0:2]
print(game)

# Describe
print(game.describe())