import pandas as pd
import numpy as np

brics = pd.read_csv('/home/gustavo-plc/PycharmProjects/dataScience/Python/brics.csv', index_col = 0)

# command above has just set the index column as 1, not 0 as default

print(brics)
print()

# HOW TO FILTER SPECIFIC DATA WITHIN A DATAFRAME

#create a sub data frame from the original one, specifying the feature (area) we want and data criteria as well to
# do the comparison
is_huge = brics['area'] > 8

print(is_huge)

#print this subset as an index from the original dataset, and get only the observations that match the criteria
print(brics[is_huge])
print()


#using boolean operators from numPy

is_medium = np.logical_and(brics['area'] > 8, brics['area'] < 10)
print(brics[is_medium])
print()

