import pandas as pd

cars = pd.read_csv('/home/gustavo-plc/PycharmProjects/dataScience/Python/cars.csv')

print(cars)
print()

#not yet what we expected

# index_col: an argument of read_csv(), that you can use to specify
# which column in the CSV file should be used as a row label

cars = pd.read_csv('/home/gustavo-plc/PycharmProjects/dataScience/Python/cars.csv', index_col = 0)

print(cars)