import numpy as np

# Numeric Python: NumPy

# the numpy's array is an alternative to lists

# good for calculations in an element-wise way

#python doesn't know how to do calculations with lists!

#example:

height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

#bmi = weight / (height ** 2) #this doesn't work!

np_height = np.array(height)
print(np_height)
np_weight = np.array(weight)
print(np_weight)


#now it works, using the numpy package. The BMI is calculated in an element-wise way!
bmi = np_weight / np_height ** 2

print(bmi)

# OBS 1 : numpy arrays can only contain on object type

print(bmi[1])
print(bmi > 23) #the result is a numpy array, containing booleans!

#to do the subsetting, we can use:

print(bmi[bmi > 23])

#exercises


baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball:

np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))




import pandas as pd
mlb = pd.read_csv('baseball.csv')

# height_in is available as a regular list
height_in = mlb['Height'].tolist()

# height_in is available as a regular list

print(height_in)



# Create a numpy array from height_in: np_height_in


np_height_in = np.array(height_in)

# Print out np_height_in

print(np_height_in)

# Convert np_height_in to m: np_height_m

np_height_m = np_height_in * 0.0254

# Print np_height_m

print(np_height_m)

print(np.array([True, 1, 2]) + np.array([3, 4, False]))

#when a Python array has different variable types True is converted to 1 and False to 0


#booleans and logical operators inside NumPy


my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5, my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11, your_house < 11))

