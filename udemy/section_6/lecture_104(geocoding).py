import pandas
from geopy.geocoders import Nominatim

url = 'http://pythonhow.com/supermarkets.csv'
url_json = 'http://pythonhow.com/supermarkets.json'

df6 = pandas.read_csv(url)

df7 = pandas.read_csv(url)
df7 = df7.set_index("Address")
df7['Continent'] = df7.shape[0]*['North America'] # add new column with same value for each row
df7['Continent'] = df7['Country'] + ',' + 'North America' # edit each row in continent column
df_t= df7.T # rows become columns
df_t['My Address'] = ['My city', 'My country', 10, 7, 'My shop', 'My state', 'My continent']

df7 = df_t.T

dm = pandas.merge(left=df6, right=df7, on='ID')
nom = Nominatim()
n = nom.geocode('3995 23rd St, San Francisco, CA 94114')
long = n.longitude
lat = n.latitude
# print(lat, long)

df = pandas.read_csv(r'C:\Users\Helen\PycharmProjects\learn_python\udemy\files\supermarkets.csv')
df['Address'] = df['Address'] + ', ' + df['City'] + ', '+ df['State'] + ', ' +  df['Country']
df['Coordinates'] = df['Address'].apply(nom.geocode)
df['Latitude'] = df['Coordinates'].apply(lambda x: x.latitude if x is not None else None)
df['Longitude'] = df['Coordinates'].apply(lambda x: x.longitude if x is not None else None)
print(df)