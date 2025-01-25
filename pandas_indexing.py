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

# make it easy to comprehend your dataset when one category is nested inside another category.

# Index temperatures by country & city: setting two hierarchical features as indexes
# this way, when printing the dataframe, two columns will be shown as indexes and the first one
# will act as the outer level and the second, the inner level

temperatures_ind2 = temperatures.set_index(['country', 'city'])
print(temperatures_ind2)
print()

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
# in a hierarchical way, in other words, taking first a country and then a city, we can
# pass them as tuples to a list, to save the rows that will be ketp.

rows_to_keep = [('Brazil', 'Rio De Janeiro'), ('Pakistan', 'Lahore')]

# Subset for rows to keep
print(temperatures_ind2.loc[rows_to_keep])
print()

# Sorting by index values
# CHANGING THE ORDER OF THE DATAFRAME ELEMENTS BY SORTING THEM BY INDEX VALUES
# DIFFERENTLY FROM BEFORE, WHEN THEY WERE SORTED BY VALUES

# use of method sort_index()

# Sort temperatures_ind by index values
# as the index was set in a nested way as country and city, the code will
# sort alphabetically first the outer level and for each one, the inner level

print(temperatures_ind2.sort_index())
print('Sorted by index')
print()

# Sort temperatures_ind by index values at the city level
# controlling the level of the sorting
print(temperatures_ind2.sort_index(level= ['city']))
print('Sorted by inner level: city')
print()

# Sort temperatures_ind by country then descending city
print(temperatures_ind2.sort_index(ascending = [True, False]))
print('Sorted by outer level: country, and showing descending city ')
print()

# SLICING (SLICE) A DATAFRAME BY VALUES

# ROWS

#IN THE OUTER LEVEL: CALL THE LOC METHOD WITH THE INDEX VALUES [THE LAST ELEMENT IS INCLUDED,
# DIFFERENTLY FROM THE LIST SLICING

# IN THE INNER LEVEL: BE CAREFUL! IT HAS TO BE CORRECTLY WRITTEN.
# WE HAVE TO PASS THE FIRST AND THE LAST POSITIONS AS TUPLES!

#COLUMNS

# TO KEEP ALL ROWS, PASS A COLON (:) AS THE FIRST ARGUMENT TO LOC
# THE SECOND ARGUMENT OF LOC RECEIVES THE FIRST AND THE LAST COLUMNS TO SLICE

#SLICE SLICING DATES: AS PASSING A DATE AS AN ARGUMENT TO THE FUNCTION LOC, WE CAN SLICE BY PARTIAL DATES

# Compared to slicing lists, there are a few things to remember.
#
#     You can only slice an index if the index is sorted (using .sort_index()).
#     To slice at the outer level, first and last can be strings.
#     To slice at inner levels, first and last should be tuples.
#     If you pass a single slice to .loc[], it will slice the rows.

# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind2.sort_index()

# Subset rows from Pakistan to Russia
# HERE WE ARE SUBSETTING THE OUTER LEVEL OF A HIERARCHICAL DATAFRAME
print(temperatures_srt.loc['Pakistan': 'Russia'])
print()

# Subset rows from Pakistan, Lahore to Russia, Moscow
# HERE WE ARE SLICING THE INNER LEVEL, SO WE MUST PASS TUPLES AS START AND END
print(temperatures_srt.loc[('Pakistan', 'Lahore'): ('Russia', 'Moscow')])
print()

# slicing in two directions dimensions at once

# Subset rows from India, Hyderabad to Iraq, Baghdad: FIRST JUST ROWS
print(temperatures_srt.loc[('India','Hyderabad'):('Iraq','Baghdad')])
print('Subset rows from India, Hyderabad to Iraq, Baghdad')
print()

# Subset columns from date to avg_temp_c: THEN COLUMNS
print(temperatures_srt.loc[:, 'date':'avg_temp_c'])
print('Subset columns from date to avg_temp_c')
print()

# Subset in both directions at once
print(temperatures_srt.loc[('India','Hyderabad'):('Iraq','Baghdad'),'date':'avg_temp_c'])
print('Subset in both directions at once')
print()

# Slicing time series (dates): dates in ISO 8601 format, that is, "yyyy-mm-dd"
# for year-month-day, "yyyy-mm" for year-month, and "yyyy" for year.


# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
temperatures_bool = temperatures[(temperatures['date'] >= '2010-01-01') & (temperatures['date'] <= '2011-12-31')]
print(temperatures_bool)
print('printing temperatures subset from 2010 to 2011')
print()

# Set date as the index and sort the index
temperatures_ind3 = temperatures.set_index('date').sort_index()

# Use .loc[] to subset temperatures_ind3 for rows in 2010 and 2011
print(temperatures_ind3.loc['2010':'2011'])
print()

# Use .loc[] to subset temperatures_ind3 for rows from Aug 2010 to Feb 2011
print(temperatures_ind3.loc['2010-08':'2011-02'])
print()

#mind-blowing: I have to have an index already set for the DF to use loc method.
# It doesn't work on DF that have no index set up.

# USING ILOC TO SLICE DF TRHOUGH ROW AND COLUMN INDEXES

# Get 23rd row, 2nd column (index 22, 1)
print(temperatures.iloc[22, 1])
print()

# Use slicing to get the first 5 rows
print(temperatures.iloc[:5])

# Use slicing to get columns 3 to 4
print(temperatures.iloc[:, 2:4])

# Use slicing in both directions at once
print(temperatures.iloc[:5, 2:4])



# SUBSETTING AND CALCULATIONS ON PIVOT TABLES

# PIVOT TABLES ARE DATAFRAMES WITH SORTED INDEXES
# ALL WE CAN DO ON DF CAN BE DONE ALSO IN PIVOT TABLES

# THE .LOC() METHOD + SLICING IS IDEAL TO SUBSETTING PIVOT TABLES

#FIRST CONVERT THE DATA ON THE DATE COLUMN TO A DATE-TIME-FORMAT
temperatures['date'] = pd.to_datetime(temperatures['date'])

print(temperatures['date'].dtype)


# Add a year column to temperatures
temperatures['year'] = temperatures['date'].dt.year
#the column year was added to DF temperatures by accessing the component year of the date

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table(values = 'avg_temp_c', index = ['country', 'city'], columns = 'year')
#the columns of the pivot table will be the years
# the values on each cell will be avg_temp
# the rows will be grouped by country and city (index field)

# See the result
print(temp_by_country_city_vs_year)
print()


# Subsetting pivot tables (subset)


# Subset for Egypt to India
temp_by_country_city_vs_year.loc['Egypt':'India']

# Subset for Egypt, Cairo to India, Delhi
temp_by_country_city_vs_year.loc[('Egypt', 'Cairo'):('India', 'Delhi')]

# Subset for Egypt, Cairo to India, Delhi, and 2005 to 2010

temp_by_country_city_vs_year.loc[('Egypt', 'Cairo'):('India', 'Delhi'), '2005':'2010']


# CALCULATING ON A PIVOT TABLE

# THE TOOL TO GET IT DONE: SPECIFY A CORRECT ARGUMENT FOR THE STSTS FUNCTION OF THE DF

# EXAMPLE: TO GET THE MEAN, YOU CAN SIMPLY WRITE THE DF'S NAME AND CALL THE MEAN METHOD.
# INSIDE THE METHOD, THE ARGUMENT AXIS HAS TO RECEIVE 'INDEX' (IF YOU WANT THE STATS TO BE CALCULATED OVER ROWS) OR
# 'COLUMNS' (IF YOU WANT THE STATS TO BE CALCULATED OVER COLUMNS).

# Get the worldwide mean temp by year
# the DF itself has an argument called axis that points to where the calculation will be done.

mean_temp_by_year = temp_by_country_city_vs_year.mean(axis = 'index')

print(mean_temp_by_year)

# Filter for the year that had the highest mean temp
print(mean_temp_by_year[mean_temp_by_year[:] == mean_temp_by_year[:].max()])

# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis = 'columns')

# Filter for the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city[:] == mean_temp_by_city[:].min()])
