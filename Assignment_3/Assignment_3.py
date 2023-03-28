#%%
from folium.plugins import FastMarkerCluster
#import contextily as ctx
import folium
import geopandas as gpd
#import matplotlib.pyplot as plt
import plotly.express as px

# load gpd

incidents_gpd = gpd.read_file('AssignmentData/incidents_clean.shp')

# plot folium map

m = folium.Map(location=[39.962334, -75.161446],zoom_start=10)
m = folium.Map(location=[39.962334, -75.161446], tiles="CartoDB dark_matter", zoom_start=15)
folium.GeoJson(data= incidents_gpd["geometry"]).add_to(m)
m

# plot folium cluster map

m.save("clusterMap.html")
m = folium.Map(location=[39.962334, -75.161446], tiles='cartodbpositron', zoom_start=10)
folium.GeoJson(data= incidents_gpd ["geometry"][0]).add_to(m)
m = folium.Map([39.962334, -75.161446], zoom_start=10, tiles='cartodbpositron')
folium.GeoJson(incidents_gpd.sample(10)).add_to(m)
m.save('acled.html')
incidents_sample = incidents_gpd.sample(500)
cmap = folium.Map(location=[39.962334, -75.161446],
                        zoom_start=10,
                        tiles='CartoDB dark_matter')
FastMarkerCluster(data=list(zip(incidents_sample.geometry.y.values, incidents_sample.geometry.x.values))).add_to(cmap)
folium.LayerControl().add_to(cmap)
cmap


# plot scatterplot

fig = px.scatter_mapbox(
    incidents_gpd,   
    lat="lat", 
    lon="lng", 
    mapbox_style="carto-darkmatter",
    zoom=10)
fig.show()




