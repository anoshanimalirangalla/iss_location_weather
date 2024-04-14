 # ISS location and weather updating Flask web application

## Objective : 
Fetch data from multiple APIs to know the whereabouts of the ISS and record weather updates. 

## Description :
In this project, I have developed a simple Python-powered flask website that does not have user input. I fetch data from several APIs to feed the site. 
Checking the current location of ISS and the current weather. 

Current location of the ISS if fetched by Open notify (http://open-notify.org/)
if the location if above land, it provides details/flags of the respective country and the weather of the respective location in Celsius. 
as the next step, it checks the distance between your location and ISS. 

## Step 1 -  fetching data from ISS API to find the location of the ISS. 

```python
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
```
## Step 2 - fetching data for weather of the location 

```python
# getting weather information 
import urllib.request  # to connect to url
import json  # to convert the data to json

# function to get weather information
def get_weather(lat,lon):
  key = 'b70d1042b2355f2d20df93fe189c57c3' # my api key

  url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"
  
  request = urllib.request.urlopen(url) # to open the url and read response
  result = json.loads(request.read()) # convert rsponse to json
  return result #return weather data as json
```
## Step 3 - fetching data for the country

```python
import urllib.request # connect the url
import json # convert the data to json

# to get information about the country
def get_country():
  url = f'https://restcountries.com/v3.1/alpha/usa' #url to fetch the data
  request = urllib.request.urlopen(url) #open url and read response
  result = json.loads(request.read()) # parse the response to json
  return result # return the data
```
## step 4  - Flask-powered web application main.py

```python
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
```
## step 5 - HTML page

```hmtl
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ISS Tracker</title>
</head>
<body>
  <center>
  <h1><b>ISS Tracker</b></h1>
  <br>
    <!-- iss location -->
    <p>Location of ISS: Latitude {{ lat }}, Longitude {{ lon }}</p>
    <br>
    <br>
    <br>
    <!-- iss static image -->
    <img src="static/iss1.jpg" alt="ISS Image" width="350">
    <br>
    <br>
    <br>
    <!-- display temperature at iss location --> 
    <p>Temperature at ISS location: {{ temp_c  }}°C</p>
    <br>
    <br>
    <!-- national flag of usa -->
    <img src="{{ flag_url }}" alt="National Flag" width="200">
    <br>
    <p>The Flag of USA</p>
    <br>
    <br>
    <!-- distance between my location and iss -->
    <p>Distance between my location and ISS: {{ distance }} kilometers</p>
  </center>
</body>
</html>
```
Original work in [Replit](https://replit.com/@a00284480/A00284480-Assignment-3)
