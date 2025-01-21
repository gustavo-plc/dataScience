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

# SORTING AND SUBSETTING DATA

# Example of sorting values: df.sort_values(["breed", "weight_kg"])

# homelessness_reg_fam = homelessness.sort_values(['region', 'family_members'], ascending = [True, False])

#subsetting columns:

# Select only the individuals and state columns, in that order
ind_state = homelessness_pd[['individuals', 'state']]
print(ind_state)
print()


# SUBSETTING ROWS: (OR FILTERING ROWS OR SELECTING ROWS)
#
# IT IS ALSO POSSIBLE TO FILTER MULTIPLE CONDITIONS AT ONCE, LIKE THE EXAMPLE BELOW:
#
# dogs[(dogs["height_cm"] > 60) & (dogs["color"] == "tan")]

#filtering by one condition
# CREATING A NEW DATAFRAME THAT RECEIVES THE SLICE OF THE HOMELESSNESS THAT CONTAINS THE DATA WHICH RESPECTS THE REQUEST

ind_gt_10k = homelessness_pd[homelessness_pd['individuals'] > 10000]
print(ind_gt_10k)

# Filter for rows where region is Mountain
mountain_reg = homelessness_pd[homelessness_pd['region'] == 'Mountain']

# See the result
print(mountain_reg)
print()

# Filter for rows where family_members is less than 1000
# and region is Pacific
fam_lt_1k_pac = homelessness_pd[(homelessness_pd['region'] == 'Pacific') & (homelessness_pd['family_members'] < 1000)]
# variable = df[(cond1) & (cond2)]

# See the result
print(fam_lt_1k_pac)
print()
# Subsetting rows by categorical variables

# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states

mojave_homelessness = homelessness_pd[homelessness_pd['state'].isin(canu)]
#to select only the rows in the column state that
# matches with at least one canu state.

# See the result
print(mojave_homelessness)
print()

# ADDING NEW COLUMNS TO EXISTING DATA (Other names: transforming, mutating, and feature engineering.)
# MAKING MY OWN COLUMNS FROM WHAT I HAVE

# Add total col as sum of individuals and family_members
homelessness_pd['total'] = homelessness_pd['individuals'] + homelessness_pd['family_members']

# Add p_homeless col as proportion of total homeless population to the state population
homelessness_pd['p_homeless'] = homelessness_pd['total'] / homelessness_pd['state_pop']

# See the result
print(homelessness_pd)