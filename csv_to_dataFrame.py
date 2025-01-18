import pandas as pd

cars = pd.read_csv('/home/gustavo-plc/PycharmProjects/dataScience/Python/cars.csv')

print(cars)
print()

#not yet what we expected

# index_col: an argument of read_csv(), that you can use to specify
# which column in the CSV file should be used as a row label

cars = pd.read_csv('/home/gustavo-plc/PycharmProjects/dataScience/Python/cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['country'])
print(type(cars['country']))

# Print out country column as Pandas DataFrame
print(cars.loc[:, ['country']])
print(type(cars[['country']]))

# Print out DataFrame with country and drives_right columns
print(cars.loc[:, ['country', 'drives_right']])

# limited way to get information from a data frame


# Print out first 3 observations
print(cars[0:3])
print()

# Print out fourth, fifth and sixth observation
print(cars[3:6])
print()
# MORE ADVANCED WAY TO GET INFORMATION FROM A DATA FRAME

# Print out observation for Japan as a Series
print(cars.loc['JAP']) # printing info in a series format
print()

# Print out observations for Australia and Egypt
print(cars.loc[['AUS', 'EG']]) # printing info in a dataframe format
print()

#selecting observations from dataframes TAG

# cars.loc['IN', 'cars_per_cap']
# cars.iloc[3, 0]
#
# cars.loc[['IN', 'RU'], 'cars_per_cap']
# cars.iloc[[3, 4], 0]
#
# cars.loc[['IN', 'RU'], ['cars_per_cap', 'country']]
# cars.iloc[[3, 4], [0, 1]]



# Print out drives_right value of Morocco: row label is MOR
print(cars.loc['MOR', 'drives_right'])
print()

# Print sub-DataFrame
print(cars.loc[['RU', 'MOR'],['country', 'drives_right']])
print()

# Print out drives_right column as Series
print(cars.loc[:, 'drives_right'])
print(type(cars.loc[:, 'drives_right']))
print()
# Print out drives_right column as DataFrame
print(cars.loc[:, ['drives_right']])
print(type(cars.loc[:, ['drives_right']]))
print()

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ['cars_per_cap', 'drives_right']])
print()

