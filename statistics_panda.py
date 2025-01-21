import pandas as pd
import numpy as np

path = '/home/gustavo-plc/PycharmProjects/dataScience/sales_subset.csv'
sales = pd.read_csv(path)

#TO KNOW A LITTLE BIT OF THE DATA, WE CAN CALL THE head() method.
# STATISTICS OVERVIEW

# Print the head of the sales DataFrame
print(sales.head())
print()

# Print the info about the sales DataFrame
print(sales.info())
print()

# Print the mean of weekly_sales
print(sales['weekly_sales'].mean())
print()

# Print the median of weekly_sales
print(sales['weekly_sales'].median())
print()

print(sales.shape)
print()
# Summarizing dates
# minimum and maximum allow you to see what time range your data covers.
# it makes sense for data format: datetime64

# Print the maximum of the date column
print(sales['date'].max())

# Print the minimum of the date column
print(sales['date'].min())
print()


# DESPITE PANDAS HAS A LOT OF METHODS, WE CAN ALSO NEED TO BUILD OUR
# OWN FUNCTIONS TO SUMMARIZE DATA

# The .agg() method allows you to apply your own custom functions to a DataFrame, as well as apply functions
# to more than one column of a DataFrame at once, making your aggregations super-efficient. For example,
# df['column'].agg(function)

# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# THE USEFUL FUNCTION IS PUT INSIDE THE AGG METHOD
# Print IQR of the temperature_c column

print(sales['temperature_c'].agg(iqr))
print()

# Update to print IQR of temperature_c, fuel_price_usd_per_l, & unemployment
# IN THIS CASE, THE FUNCTION IS BEING APPLIED TO MORE THAN ONE COLUMN AT ONCE

print(sales[['temperature_c', 'fuel_price_usd_per_l', 'unemployment']].agg(iqr))
print()

# TO APPLY TWO DIFFERENT FUNCTIONS TO MORE THAN ONE COLUMN, THE COLUMNS HAS TO BE SPECIFIED
# BEFORE THE METHOD AGG IS CALLED. MOREOVER, THE AGG METHOD HAS TO BE CALLED WITH SQUARE BRAKETS
# AND A COMMA SEPARATING THE TWO FUNCTIONS INSIDE, LIKE THE EXAMPLE:

print(sales[['temperature_c', 'fuel_price_usd_per_l', 'unemployment']].agg([iqr, np.median]))