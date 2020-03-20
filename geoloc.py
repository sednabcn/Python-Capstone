import requests
url = 'https://maps.googleapis.com/maps/api/geocode/json'
params = {'sensor': 'false', 'address': 'Regent Park, Toronto'}
r = requests.get(url, params=params)
results = r.json()['results']
#location = results[0]['geometry']['location']
#location['lat'], location['lng']
print(results)
import geocoder
g=geocoder.google('Regent Park, Toronto')
print(g.latlng)
print(g.json)
print(g.geojson)
