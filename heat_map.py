#Runs the stravaAPI script to create a pandas DataFrame of Latitude and Longitude points.
#The script then uses the pandas DataFrame to build a heat map of all the activites uploaded to Strava by the athlete.

import requests
import urllib3
import polyline
import pandas as pd


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth_url = "https://www.strava.com/oauth/token"
activites_url = "https://www.strava.com/api/v3/athlete/activities"

#THE ONLY THING YOU'LL NEED TO CHANGE (if i did this right lol)
payload = {
    'client_id': "xxxxx", #change this
    'client_secret': "xxxxxxxx", #change this
    'refresh_token': "xxxxxxxxx", #change this
    'grant_type': "refresh_token",
    'f': 'json'
}

print("Requesting Token...\n")
res = requests.post(auth_url, data=payload, verify=False)
access_token = res.json()['access_token']
print("Access Token = {}\n".format(access_token))

header = {'Authorization': 'Bearer ' + access_token}
my_dataset = []
page_number = 1
param = {'per_page': 200, 'page': page_number}

while requests.get(activites_url, headers=header, params=param).json():
    print("Loading page... ", page_number)
    res = requests.get(activites_url, headers=header, params=param).json()
    my_dataset.extend(res)
    page_number += 1
    param = {'per_page': 200, 'page': page_number}
print("Done loading Strava data.")

print("decoding polyline data to latitude and longitude points")
map_points = []
for run in my_dataset:
    if run["map"]["summary_polyline"]:
        map_points.extend(polyline.decode(run["map"]["summary_polyline"]))

print("Formating resulting points into a Pandas DataFrame")
run_points = pd.DataFrame (map_points, columns = ('Latitude', 'Longitude'))
print(run_points)

print("Building heat map...")
import plotly.graph_objects as go
fig = go.Figure(go.Densitymapbox(lat=run_points.Latitude, lon=run_points.Longitude,
                                 radius=5))
fig.update_layout(mapbox_style="stamen-terrain", mapbox_center_lon=180)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
print("Build Complete.")
