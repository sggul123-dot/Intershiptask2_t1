import requests
import folium

# Get location data from IP
url = "http://ip-api.com/json/"
response = requests.get(url)
data = response.json()

lat = data['lat']
lon = data['lon']
city = data['city']
country = data['country']

print("City:", city)
print("Country:", country)

# Create map
map = folium.Map(location=[lat, lon], zoom_start=10)
folium.Marker([lat, lon], popup=city).add_to(map)

# Save map
map.save("location_map.html")
print("Map saved as location_map.html")