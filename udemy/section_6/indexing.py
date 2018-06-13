import pandas

from udemy.config import path_to_test_files

path = commas_sep = path_to_test_files + '/' + 'supermarkets.json'
df = pandas.read_json(path)

df.set_index("Address") # not an inplace operator, will not store value in df

# label based indexing

df_i = df.set_index("Address")
slice = df_i.loc["735 Dolores St":"332 Hill St", "Country": "ID"] # "ID" and "332 Hill St" are inclusive
# print(slice)

intersec = df_i.loc["332 Hill St", "Country"]
# print(intersec)

all_countries_list = list(df_i.loc[:, "Country"])
# print(all_countries_list)

index_slice = df_i.iloc[1:5, 1:3] # 3 is not inclusive; 1:5 rows, 1:3 columns
# print(index_slice)

d = df_i.ix[3, "Name"] # prints row with index 3 and column with label Name
print(d)

d1 = df_i.ix[3, 4] # prints row with index 3 and column with index 4
print(d1)