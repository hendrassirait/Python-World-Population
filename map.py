import folium
import pandas
import math

data = pandas.read_csv("worldcities.csv")

lat = list(data["lat"])
lon = list(data["lng"])
populasi  = list(data["population"])
kota = list(data["city"])

def warna_kota(population):
	if math.isnan(population):
		return 'grey'
	elif population < 10000:
		return 'green'
	elif 10000 <= population < 20000:
		return 'orange'
	elif 20000 <= population < 30000:
		return 'brown'
	elif 40000 <= population < 50000:
		return 'yellow'	
	elif 60000 <= population < 70000:
		return 'blue'
	elif 80000 <= population < 90000:
		return 'gold'
	elif 90000 <= population < 100000:
		return 'pink'
	else:
		return 'red'

map = folium.Map(location=[-2.147394,122.550288],zoom_start=5)

fgk = folium.FeatureGroup(name='Populasi Kota')

for lt, ln, pop, kot in zip(lat, lon, populasi, kota):
	fgk.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup="kota "+kot+", Populasi : "+str(pop)+" Jiwa", fill_color=warna_kota(pop), color = 'grey', fill_opacity=0.7))

fgn = folium.FeatureGroup(name='Populasi Negara')


fgn.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='UTF-8-sig').read(), style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 
	'orange' if 10000000 <= x['properties'] ['POP2005'] <20000000 else 
	'brown' if 20000000 <= x['properties'] ['POP2005'] <30000000 else 
	'yellow' if 40000000 <= x['properties'] ['POP2005'] <20000000 else 
	'blue' if 50000000 <= x['properties'] ['POP2005'] <60000000 else 
	'gold' if 70000000 <= x['properties'] ['POP2005'] <80000000 else 
	'white' if 90000000 <= x['properties'] ['POP2005'] <100000000 else 'red'}))

map.add_child(fgk)
map.add_child(fgn)
map.add_child(folium.LayerControl()) 
map.save("Map1.html")