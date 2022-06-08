# Personal Strava Heat Map

Genrates an interactive Heat Map of all your activites uploaded to Strava. After gaining authorization to the Strava API and genrating a refresh token, the script pulls all exisiting activity map data in teh form of encoded polylines. Using a simple package to decode the polyline into latitude and longidude pairs, the script formats the points into a Pandas DataFrame. The DataFrame is then used to build a Heat Map using the Poltly Mapbox Density Heatmap module.

<img width="1351" alt="IMG_9037" src="https://user-images.githubusercontent.com/59592139/172694183-83fe1f8d-284a-45a2-a2f6-68892d28be43.png">

