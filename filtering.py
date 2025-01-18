import pandas as pd
import numpy as np

brics = pd.read_csv('/home/gustavo-plc/PycharmProjects/dataScience/Python/brics.csv', index_col = 0)

cars = pd.read_csv('/home/gustavo-plc/PycharmProjects/dataScience/Python/cars.csv', index_col = 0)
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

# SELECTING DATA FROM ANOTHER CSV FILE FOR WHICH THE VALUES FOR DRIVES RIGHT IS TRUE

dr = cars['drives_right']
print(dr)

sel = cars[dr]
print(sel)
print()
# ANOTHER SIMPLER WAY:

sel = cars[cars['drives_right']]
print(sel)
print()
#ANOTHER EXAMPLE:

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars['cars_per_cap']
print(cpc)
print()

many_cars = cpc > 500
print(many_cars)
print()

car_maniac = cars[many_cars]  #indexing the original dataset with a boolean array

# Print car_maniac
print(car_maniac)
print()

# MORE advanced filtering operations!!

