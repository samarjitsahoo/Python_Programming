import numpy as np
import pandas as pd

# Load the dataset
movie = pd.read_csv('C:/Users/samar/Practice/Python_Practice/Python_Data_Frame/bollywood.csv')

# Display the dataset
print(movie)

# Check the type of movie
print(type(movie))

# Display the first two rows
print(movie.head(2))

# Rename columns
movie = movie.rename(columns={'lead': 'actor'})
print(movie)

# Accessing Single Row
single_row = movie[movie.movie == 'Battalion 609']
print(single_row)

# Accessing Single Column
single_column = movie['actor']
print(single_column)

# Accessing Multiple Columns
mul_col = movie[['movie', 'actor']]
print(mul_col)

# Using loc for data location
print(movie.loc[2, 'actor'])

# Display the movie of the 1st Row
print(movie.loc[0, 'movie'])

# Display data in a Range of Rows
print(movie.loc[2:5, ['movie', 'actor']])

# Display the columns movie and actor from rows 1 to 4
print(movie.loc[1:4, ['movie', 'actor']])

# Include all cols
print(movie.loc[2:5])

# Use of iloc(Index Location)
print(movie.iloc[2:7, 1]) 

# iloc doesn't include the last range of the row & column
print(movie.iloc[2:7, 0:2])

# Display the columns movie and actor for rows 0 to 5
print(movie.iloc[0:6])

# Replacing the Content
movie = movie.iloc[2:7, 0:2]
print(movie)

# Describe
print(movie.describe())