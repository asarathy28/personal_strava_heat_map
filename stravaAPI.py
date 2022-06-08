#Script that pulls your activites map data and exports it as latitude and longitude points in csv file.
#The file is formated so it can be used for a heat map.

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
df = pd.DataFrame (map_points, columns = ('Latitude', 'Longitude'))
print (df)

df.to_csv('destination_file.csv')
print("Export complete.")
