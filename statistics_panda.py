import pandas as pd

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

# Summarizing dates

