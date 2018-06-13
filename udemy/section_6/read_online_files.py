import pandas

url = 'http://pythonhow.com/supermarkets.csv'
url_json = 'http://pythonhow.com/supermarkets.json'

df = pandas.read_csv(url)
print(df)

df1 = pandas.read_json(url_json)
print(df1)

