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