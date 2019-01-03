import folium
import pandas

data = pandas.read_csv("Volcanoes.txt") #Using Pandas lib to call in txt file and putting it in a var

lat = list(data["LAT"])  # Assinging lat to read in all the lat info in the txt file
log = list(data["LON"]) # Assinging Log to a list that reads the data and extracts the values Under LON keyword
elev = list (data["ELEV"])

def color_producer(elevation): #Simply Function that takes the elevation and if it's above a certain number change color
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location= [38.58, -99.09] ,zoom_start =6, tiles= "Mapbox Bright") # Map object equals the starting Coordinantes of our intial view

fgv = folium.FeatureGroup (name="Volcanoes") #Creates a features group to view our variables

for lt, lg , el in zip (lat,log,elev): # all three data type in file
    fgv.add_child(folium.CircleMarker(location = [lt,lg] , radius = 7.0, popup = str(el) + "m" , # Add markers for each lat and long
    fill_color = color_producer(el), color = "grey", fill_opacity = 0.7)) #use the function earlier based on the eval values of each volcano

fgp = folium.FeatureGroup (name="Population") #Our second feature group that focuses on population

fgp.add_child(folium.GeoJson(data = open("World.json", "r", encoding='UTF-8-sig').read(),
style_function = lambda x:{'fillColor':"Green" if x["properties"]["POP2005"] < 10000000
else "Orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "RED"})) #Added Yellow in the Json File

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
