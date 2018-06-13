import pandas

from udemy.config import path_to_test_files

path = commas_sep = path_to_test_files + '/' + 'supermarkets.json'
df = pandas.read_json(path)
df = df.set_index("Address")

df.drop("City", 1) # delete column -> 1; not inplace operator
df.drop("332 Hill St", 0) # delete row -> 0