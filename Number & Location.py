import phonenumbers
import opencage
import folium
from Mynumber import Phone_Number

# Extract Country Name
from phonenumbers import geocoder
p = phonenumbers.parse(Phone_Number)
country_Location = geocoder.description_for_number(p, "en")
print(f"Country Name: {country_Location}")

# Extract Service Provider Name
from phonenumbers import carrier
Service_Provider = phonenumbers.parse(Phone_Number)
print(f"Service Provider Name: {carrier.name_for_number(Service_Provider, 'en')}")

# Find Location
from opencage.geocoder import OpenCageGeocode
API = "144eb535f56d493bb1639ebf66fa1ec2"
geocoder = OpenCageGeocode(API)
query = country_Location
results = geocoder.geocode(query)
print(f"Longitude & Latitude : {results}")
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)  
  
# Google Map
mymap = folium.Map(country_Location = [lat,lng],zoom_start= 9)
folium.Marker([lat,lng], popup= country_Location).add_to(mymap)
mymap.save(r"Downloads\GoogleMap.html",close_file=True)
