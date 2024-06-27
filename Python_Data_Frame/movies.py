import numpy as np
import pandas as pd

# Load the dataset
movies_data = pd.read_csv('C:/Users/samar/Downloads/movies.csv')

# Print the dataframe to understand its structure
print(movies_data)

# Print the type of the dataframe
print(type(movies_data))

# Display the first few rows of the dataframe
print(movies_data.head(2))

# Rename columns
movies_data = movies_data.rename(columns={'runtime': 'duration'})
print(movies_data)

# Accessing Single Row based on condition
single_movie = movies_data[movies_data.title_x== 'Battalion 609']
print(single_movie)

# Accessing Single Column
single_column = movies_data['title_x']
print(single_column)

# Accessing Multiple Columns
multiple_columns = movies_data[['title_x', 'title_y']]
print(multiple_columns)

# Using loc for specific location in data
print(movies_data.loc[2, 'title_y'])
print(movies_data.loc[0, 'genres'])

# Display data in a Range of Rows and Columns
print(movies_data.loc[2:5, ['title_x', 'title_y']])

# Display specific columns for a range of rows
print(movies_data.loc[1:4, ['imdb_id', 'imdb_rating']])

# Include all columns for a range of rows
print(movies_data.loc[2:5])

# Use of iloc (Index Location)
print(movies_data.iloc[2:7, 2])

# iloc doesn't include the last range of the row & column
print(movies_data.iloc[2:7, 0:3])

# Display specific columns for rows 0 to 5
print(movies_data.iloc[0:6])

# Replacing the content
movies_data = movies_data.iloc[2:7, 0:4]
print(movies_data)

# Describe
print(movies_data.describe())
