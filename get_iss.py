# find the location of ISS

import urllib.request  # to connect to url
import json  # to convert the data to json

# find the location of iss 
def iss_loc():
  url = "http://api.open-notify.org/iss-now.json" # url to get the location of iss
  request = urllib.request.urlopen(url) # to open the url and read response
  result = json.loads(request.read()) # convert rsponse to json
  #print(result)
  lat = result['iss_position']['latitude']
  lon = result['iss_position']['longitude']
  #print(lat,lon)
  #print("https://www.google.com/maps/place/" + lat + "+"+ lon) #passing lat and long to google maps.
  return lat, lon 
