import folium
import pandas

df = pandas.read_csv('data.txt')

def color(elev):
    if elev in range(0, 1000):
        col = "green"
    elif elev in range(1000, 3000):
        col = "orange"
    else:
        col = "red"
    return col

map = folium.Map(location=[df['LAT'].mean(), df['LON'].mean()],
                 zoom_start=12,
                 tiles='Stamen Terrain')

for lat, lon, name, elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
    map.simple_marker(location=[lat, lon],
                      popup=name,
                      marker_color=color(elev)
                      )




map.create_map(path="test.html")


