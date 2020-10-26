import folium
import pandas

df1 = pandas.read_csv("Test Files/MapData.csv")
lat = list(df1["Latitude"])
lon = list(df1["Longitude"])
elev = list(df1["Elevation"])

def setcolour(elevation):
    if elevation <2:
        return 'green'
    elif elevation <3:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[51.587363, 0.601363], zoom_start=15, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
#    fg.add_child(folium.Marker(location=[lt, ln], popup="df1.Name", icon=folium.Icon(color="green")))
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el) + " m",
     fill_color=setcolour(el), color = 'grey', fill_opacity=0.7))

map.add_child(fg)

map.save("Mapping/Map1.html")

