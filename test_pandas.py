# USING DATAFRAMES TO COMPILE INFORMATION: A NEW DATA STRUCTURE APPROACH
# It's basically a way to store tabular data where you can label the rows and the columns.

import pandas as pd

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)
print()
#the row labels are not correctly set. We need to correct them

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)
print()

# To iterate over a dictonary obtaining its keys and values:

# Definition of dictionary
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin',
          'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw', 'austria': 'vienna'}

# Iterate over europe

for k, v in europe.items(): #the method items() has to be used to do so
    print('the capital of ' + str(k) + ' is ' + str(v))
print()
# DATA MANIPULATION WITH Pandas!

# When you get a new DataFrame to work with, the first thing you need to do is explore it and see what it contains.
# There are several useful methods and attributes for this.
#
#     .head() returns the first few rows (the “head” of the DataFrame).
#     .info() shows information on each of the columns, such as the data type and number of missing values.
#     .shape returns the number of rows and columns of the DataFrame.
#     .describe() calculates a few summary statistics for each column.

path = '/home/gustavo-plc/PycharmProjects/dataScience/homelessness.csv'
homelessness_pd = pd.read_csv(path)

print(homelessness_pd.head())
print()
print(homelessness_pd.info())
print()
print(homelessness_pd.describe())
print()

# DataFrames have three components: values, a column index, and a row index.
#
#     .values: A two-dimensional NumPy array of values. [[a, b]...[x, y]]
#     .columns: An index of columns: the column names.
#     .index: An index for the rows: either row numbers or row names.

print(homelessness_pd.values)
print()
print(homelessness_pd.columns)
print()
print(homelessness_pd.index)
print()

