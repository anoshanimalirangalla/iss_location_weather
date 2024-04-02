from flask import Flask, render_template
import requests
import urllib.request
import json
import geopy.distance 

app = Flask(__name__)

# import fuctions to get iss_loc, weather, country, and distance.

from get_iss import iss_loc
from get_weather import get_weather
from get_country import get_country
from get_distance import dist 




# route for the home page
@app.route('/')
def home():
  #where the ISS space station is;
  data = iss_loc()
  lat, lon = data[0],data[1]
  #weather information
  weather = get_weather(lat,lon)
  #print(weather)
  temp_c = round(weather["main"]["temp"] - 273.15,2)
  #print(str(temp_c)+" C ")
  # country flag
  flag_url = get_country()[0]["flags"]["png"]
  #print(flag_url)


  # distance from your location to the ISS
  distance = dist(lat,lon,46.4997065,-80.9969685) #my location cordinates - 284,Notre Dame Ave, Sudbury
  #print(f"Your location is {distance} km from the ISS")


 # rennder the html template with data
  return render_template("index.html",lat=lat,lon=lon,temp_c=temp_c,distance=distance,flag_url=flag_url)
  
if __name__ == '__main__':
  # runinng the flask application
    app.run(host='0.0.0.0', port=8080)
