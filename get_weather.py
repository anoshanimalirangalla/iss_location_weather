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
