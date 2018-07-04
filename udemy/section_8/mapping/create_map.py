import folium
map = folium.Map(location=[50.45466, 30.5238], tiles='Mapbox Bright')
fg = folium.FeatureGroup(name='My Map')
for coordinates in [[46.469391, 30.740883], [48.45, 34.98333], [50.45466, 30.5238], [48.41, 29.14]]:
	fg.add_child(folium.Marker(location=coordinates,
								popup='Hi, I am a Marker', icon=folium.Icon(color='green')))
map.add_child(fg)
map.save('map1.html')




