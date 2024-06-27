import numpy as np
import pandas as pd

# Load the IPL matches dataset
ipl_matches = pd.read_csv('C:/Users/samar/Downloads/ipl-matches.csv')

# Display the dataset
print(ipl_matches)

# Display the type of the dataset
print(type(ipl_matches))

# Display the first two rows
print(ipl_matches.head(2))

# Rename columns
ipl_matches = ipl_matches.rename(columns={'ID': 'Regd No'})
print(ipl_matches)


# Accessing Single Column
single_column = ipl_matches['City']
print(single_column)

# Display specific columns
mul_col=ipl_matches[['Regd No', 'City', 'Date', 'Season']]
print(mul_col)

# Accessing a single row
single_match = ipl_matches.iloc[0]
print(single_match)

# Accessing a single column
team1_column = ipl_matches['Team1']
print(team1_column)

# Accessing multiple columns
teams_column = ipl_matches[['Team1', 'Team2']]
print(teams_column)

# Using loc for accessing specific data
print(ipl_matches.loc[2, 'Season'])

# Displaying the ID of the first row
print(ipl_matches.loc[0, 'Regd No'])

# Displaying data in a range of rows
print(ipl_matches.loc[2:5, ['Season', 'MatchNumber']])

# Displaying specific columns for a range of rows
print(ipl_matches.loc[1:4, ['Regd No', 'City', 'Date']])

# Include all columns for a range of rows
print(ipl_matches.loc[2:5])

# Using iloc (Index Location)
print(ipl_matches.iloc[2:7, 2])

# iloc doesn't include the last range of the row & column
print(ipl_matches.iloc[2:7, 0:3])

# Displaying specific columns for rows 0 to 5
print(ipl_matches.iloc[0:6])

# Replacing the content
ipl_matches_subset = ipl_matches.iloc[2:7, 0:4]
print(ipl_matches_subset)

# Describe the dataset
print(ipl_matches.describe())
