
#Run this to see a Heat Map of all my runs uploaded to Strava.
#~up to date through April 2020 - June 2022~

import pandas as pd
run_points = pd.read_csv("ajays_strava_map_points.csv")

import plotly.graph_objects as go
fig = go.Figure(go.Densitymapbox(lat=run_points.Latitude, lon=run_points.Longitude,
                                 radius=5))
fig.update_layout(mapbox_style="stamen-terrain", mapbox_center_lon=180)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
