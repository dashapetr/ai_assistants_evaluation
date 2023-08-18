# visualization for geo data


import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln in zip(lat, lon):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup="Hi", fill_color="red", color="grey"))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
                             style_function=lambda x: {"fillColor": "green" if x["properties"]["POP2005"] < 10000000
                             else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"}))
