import os
import pandas

from udemy.config import path_to_test_files

list_files = os.listdir(path_to_test_files)
csv_file_name = 'supermarkets'
path_to_file = '{path_to_dir}/{file}.'.format(path_to_dir=path_to_test_files, file=csv_file_name)
csv = path_to_file + 'csv'
json = path_to_file + 'json'
xlsx = path_to_file + 'xlsx'
commas_sep = path_to_test_files + '/' + 'supermarkets-commas.txt'
semi_columns = path_to_test_files + '/' + 'supermarkets-semi-colons.txt'

# read csv file
df1 = pandas.read_csv(csv) # header=None
df1.set_index('ID')
shape_df1 = df1.shape
print(df1)

# read json file
df2 = pandas.read_json(json)
df2.set_index('ID')
shape_df2 = df2.shape
print(df2)

# read excel file
df3 = pandas.read_excel(xlsx, sheet_name=0)
shape_df3 = df3.shape
print(df3)

df4 = pandas.read_csv(commas_sep)
print(df4)

df5 = pandas.read_csv(semi_columns, sep=';')
print(df5)

