import requests
import json 
from datetime import datetime

url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
response = requests.get(url)
eq = response.json() #can also use json.loads()

count = len(eq["features"])

print("There were " + str(count) + " earthquakes in the last hour:\n")

for key in range(len(eq["features"])):
  magnitude = eq["features"][key]["properties"]["mag"]
  place = eq["features"][key]["properties"]["place"]

  for time in range(len(eq["features"])):
    time = eq["features"][key]["properties"]["time"]/1000
    hour = datetime.fromtimestamp(time).strftime("%H:%M:%S")
    date = datetime.fromtimestamp(time).strftime("%Y-%m-%d")
  
  print(f"A magnitude {magnitude} earthquake occured {place} on {date} at {hour}.\n")
