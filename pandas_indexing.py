import pandas as pd

path = '/home/gustavo-plc/PycharmProjects/dataScience/temperatures.csv'
temperatures = pd.read_csv(path)

# Explicit indexes
# Setting and removing indexes

# Look at temperatures
print(temperatures)
print()

# Set the index of temperatures to city
# THE INDEX IS NO MORE A COLUMN OF INTEGERS. THIS INDEX COLUMN WAS REPLACED BY THE CITY COLUMN
temperatures_ind = temperatures.set_index('city')

# Look at temperatures_ind
print(temperatures_ind)
print()

# Reset the temperatures_ind index, keeping its contents
#note that the column that was set to be the index has changed its position.
print(temperatures_ind.reset_index())
print()

# Reset the temperatures_ind index, dropping its contents
# This removed the column that was set to be the index column
print(temperatures_ind.reset_index(drop = True))
print()

# Setting an index allows more concise code for subsetting for rows of a categorical variable via .loc[]

# Subsetting with .loc[]
# .loc[]: a subsetting method that accepts index values.

# Make a list of cities to subset on
#just creating a simple list
cities = ['Moscow', 'Saint Petersburg']

# Subset temperatures using square brackets
#showing just the rows of the original dataset which has Moscow and St. Pet. as the city
print(temperatures[temperatures['city'].isin(cities)])
print()

# Subset temperatures_ind using .loc[]
#another way to do the subsetting
print(temperatures_ind.loc[cities])
print()

# THE IDEA HERE IS TO SET AN INDEX TO FACILITATE THE USE OF .LOC() METHOD
# THIS MAKES THE CODE EASY TO UNDERSTAND AND IT IS BEST VISUALLY


# HIERARCHICAL INDEXES

# Setting multi-level indexes

# Index temperatures by country & city: setting two hierarchical features as indexes
# this way, when printing the dataframe, two columns will be shown as indexes and the first one
# will act as the outer level and the second, the inner level

temperatures_ind2 = temperatures.set_index(['country', 'city'])
print(temperatures_ind2)
print()

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
#rows_to_keep = [____]

# Subset for rows to keep
#print(temperatures_ind2.____)





