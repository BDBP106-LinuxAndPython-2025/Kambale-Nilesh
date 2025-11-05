# (1) Create a module, CSVProcessor. It should contain functions for loading CSV data
# from an external file (titanic.csv), calculating total number of columns, calculating total
# number of rows and filling missing values in any column with zero. Use Pandas read csv
# and other Pandas and Numpy functions. Import this module into another program and
# demonstrate invoking these methods.

import CSVProcessor as sv

data = sv.csv_reader('titanic.csv')

print('Total columns in csv file ')
print(sv.columns_no(data))

print('Total rows in csv file ')
print(sv.rows_no(data))

df_filled = sv.fill_missing(data)
print('filling the missing values with zeros')
print(df_filled.head(100))

