#%%
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

pn = gpd.read_file('AssignmentData/Neighborhoods_Philadelphia/Neighborhoods_Philadelphia.shp')
#pn.head(5)
#pn.plot()

incidents_df = pd.read_csv('AssignmentData/incidents.csv')
incidents_df.head(5)
incidents_geo_df = gpd.GeoDataFrame(
    incidents_df, 
    geometry=gpd.points_from_xy(incidents_df.lng, incidents_df.lat,crs='EPSG:4326')
)
incidents_geo_df.head(5)
#incidents_geo_df.plot()
#incidents_geo_df.crs
incidents_geo_df = incidents_geo_df[(incidents_geo_df.lat > 38)]
#incidents_geo_df.plot()
incidents_geo_df.to_file('AssignmentData/incidents.shp')  
pn.crs
incidents_geo_df.crs
incidents_projected_geo_df = incidents_geo_df.to_crs(epsg=2272)
incidents_projected_geo_df.crs
fig, ax = plt.subplots()
incidents_projected_geo_df.plot(ax=ax)
incidents_projected_geo_df.plot(ax=ax, color='red')