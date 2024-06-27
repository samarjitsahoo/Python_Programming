import numpy as np
import pandas as pd

# Load the dataset
views = pd.read_csv('C:/Users/samar/Practice/Python_Practice/Python_Data_Frame/subs.csv')

# Display the dataset
print(views)

# Check the type of views
print(type(views))

# Display the first two rows
print(views.head(2))

# Rename columns
views = views.rename(columns={'Subscribers gained': 'Subs_Gained'})
print(views)

# Accessing Single Row
single_row = views[views.Subs_Gained == 2]
print(single_row)

# Accessing Single Column
single_column = views['Subs_Gained']
print(single_column)

# Using loc for data location
print(views.loc[2, 'Subs_Gained'])

# Display the Subs_Gained of the 1st Row
print(views.loc[0, 'Subs_Gained'])

# Include all cols
print(views.loc[2:5])

# Describe
print(views.describe())