from xmlrpc.client import METHOD_NOT_FOUND

import pandas as pd
import numpy as np
from matplotlib.colors import ColorSequenceRegistry

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
print()

# CUMMULATIVE STATISTICS

# Sort sales_1_1 by date
sales_1_1 = sales.sort_values('date')
print(sales_1_1['date'])
print()

# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1['cum_weekly_sales'] = sales['weekly_sales'].cumsum()
print(sales_1_1.head())
print()

# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1['cum_max_sales'] = sales['weekly_sales'].cummax()
print(sales_1_1.head())
print()

# See the columns you calculated
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])

# COUNTING: DATA MANIPULATION WITH PANDAS
# SUMMARIZING CATEGORICAL DATA

# Dropping duplicates

# Drop duplicate store/type combinations: using method drop_duplicates applied to the target column(s)-[1 or more]
store_types = sales.drop_duplicates(subset = ['store', 'type'])
#removing the entries that have the same store name AND same type
print(store_types.head())
print('Drop duplicate store/type combinations')
print()

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset = ['store', 'department'])
#removing entries that have same store name and same department
print(store_depts.head())
print('Drop duplicate store/department combinations')
print()

# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales['is_holiday'] == True].drop_duplicates(subset = 'date')
#the line above creates a subset from sales that has only the entries which is_holyday is True.
#Then, the date duplicates are removed
#the result is saved on a new dataframe, called holiday_dates

# Print date col of holiday_dates
print(holiday_dates['date'])
print('Subset the rows where is_holiday is True and drop duplicate dates')
print()

# AFTER REMOVING DUPLICATES, IT'S TIME TO COUNT CATEGORICAL VARIABLES

# Count the number of stores of each type, using value_counts() method
store_counts = store_types['type'].value_counts()
print(store_counts)
print('Count the number of stores of each type')
print()


# Get the proportion of stores of each type
store_props = store_types['type'].value_counts(normalize= True) #to get proportions , instead of just numbers
print(store_props)
print('to get proportions , instead of just numbers')
print()

# Count the number of stores for each department and sort
dept_counts_sorted = store_depts['department'].value_counts(sort = True)
print(dept_counts_sorted)
print('Count the number of stores for each department and sort')
print()

# Get the proportion of stores in each department and sort
dept_props_sorted = store_depts['department'].value_counts(sort= True, normalize=True)
print(dept_props_sorted)
print('Get the proportion of stores in each department and sort')
print()

# INTRODUCING THE GROUPBY METHOD
# IT IS USEFUL FOR OBTAINING STATISTICS VALUES OF AN ATTRIBUTE
# IN RESPECT OF ANOTHER ATTRIBUTE
#
# FOR EXAMPLE: TO EASILY CALCULATE THE MEAN WEIGHT (OR MORE THAN JUST ONE VARIABLE) FROM ALL DOG COLORS
# (AND BREEDS FOR EXAMPLE) WE CAN GROUP BY THE COLOR (AND BREED...) VARIABLE, SELECT THE WEIGHT (AND HEIGHT FOR EXAMPLE)
# COLOR AND TAKE THE MEAN OR USE THE AGG METHOD TO GET MULTIPLE STATISTICS

# MULTIPLE COMBINATIONS CAN BE MADE

