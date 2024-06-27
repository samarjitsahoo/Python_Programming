import numpy as np
import pandas as pd

# Load the "diabetes.csv" dataset
diabetes = pd.read_csv('C:/Users/samar/Downloads/diabetes.csv')

# Display the dataset and its type
print(diabetes)
print(type(diabetes))

# Display the first two rows
print(diabetes.head(2))

# Rename columns
diabetes = diabetes.rename(columns={'DiabetesPedigreeFunction':'DiabetesFunction'})
print(diabetes)

# Accessing Single Row
single_row = diabetes[diabetes['Pregnancies'] == 1]
print(single_row)

# Accessing Single Column
single_column = diabetes['Glucose']
print(single_column)

# Accessing Multiple Columns
multiple_columns = diabetes[['Pregnancies', 'Glucose', 'BloodPressure']]
print(multiple_columns)

# Using location in data
print(diabetes.loc[2, 'Glucose'])

# Display the 'Outcome' of the first row
print(diabetes.loc[0, 'Outcome'])

# Display data in a Range of Rows
print(diabetes.loc[2:5, ['Glucose', 'BloodPressure']])

# Display the columns 'Pregnancies', 'Glucose', and 'BloodPressure' from rows 1 to 4
print(diabetes.loc[1:4, ['Pregnancies', 'Glucose', 'BloodPressure']])

# Include all columns
print(diabetes.loc[2:5])

# Use of iloc (Index Location)
print(diabetes.iloc[2:7, 2])

# iloc doesn't include the last range of the row & column
print(diabetes.iloc[2:7, 0:3])

# Display the columns 'Pregnancies', 'Glucose', 'BloodPressure' for rows 0 to 5
print(diabetes.iloc[0:6, [0, 1, 2]])

# Replacing the Content
diabetes_subset = diabetes.iloc[2:7, 0:4]
print(diabetes_subset)

# Describe
print(diabetes_subset.describe())
