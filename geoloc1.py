from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="Ruperto")
location = geolocator.geocode("Downton Toronto, Regent Park")
print(location.address)
print((location.latitude, location.longitude))
print(location.raw)

