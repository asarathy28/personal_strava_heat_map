# Personal Strava Heat Map

Generates an interactive Heat Map of all your activities uploaded to Strava. After gaining authorization to the Strava API and generating a refresh token, the script pulls all existing activity map data in the form of encoded polylines. Using a simple package to decode the polyline into latitude and longitude pairs, the script formats the points into a Pandas DataFrame. The DataFrame is then used to build a Heat Map using the Poltly Mapbox Density Heatmap module.

<img width="1351" alt="IMG_9037" src="https://user-images.githubusercontent.com/59592139/172694183-83fe1f8d-284a-45a2-a2f6-68892d28be43.png">

