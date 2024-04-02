import urllib.request # connect the url
import json # convert the data to json

# to get information about the country
def get_country():
  url = f'https://restcountries.com/v3.1/alpha/usa' #url to fetch the data
  request = urllib.request.urlopen(url) #open url and read response
  result = json.loads(request.read()) # parse the response to json
  return result # return the data 
