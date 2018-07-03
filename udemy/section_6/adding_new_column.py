import pandas

from udemy.config import path_to_test_files

path = commas_sep = path_to_test_files + '/' + 'supermarkets.json'
df = pandas.read_json(path)
df_1 = df.set_index("Address")

df_1['Continent'] = df_1.shape[0]*['North America'] # add new column with same value for each row

df_1['Continent'] = df_1['Country'] + ',' + 'North America' # edit each row in continent column

df_t= df_1.T # rows become columns

df_t['My Address'] = ['My city', 'My country', 10, 7, 'My shop', 'My state', 'My continent']

df_1 = df_t.T
print(df_1)

