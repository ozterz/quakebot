import requests
import json 
from datetime import datetime

url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
response = requests.get(url)
eq = response.json() #can also use json.loads()

eq_list = []

print("There were 9 earthquakes in the last hour:\n")

for key in range(len(eq["features"])):
  magnitude = eq["features"][key]["properties"]["mag"]
  eq_list.append(magnitude)

  place = eq["features"][key]["properties"]["place"]
  eq_list.append(place)

  for time in range(len(eq["features"])):
    time = eq["features"][key]["properties"]["time"]/1000
    hour = datetime.fromtimestamp(time).strftime("%H:%M:%S")
    eq_list.append(hour)
    date = datetime.fromtimestamp(time).strftime("%Y-%m-%d")
    eq_list.append(date)
  
  "-Magnitude {} {} at {} {} UTC.".format(
    magnitude,
    place,
    date,
    hour
  )
  print(f"A magnitude {magnitude} earthquake occured {place} on {date} at {hour}.\n")