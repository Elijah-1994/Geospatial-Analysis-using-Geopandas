#%%
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt


def load_shp_file(shapefile) -> str:
    philadelphia_neighborhoods = gpd.read_file(shapefile)
    philadelphia_neighborhoods.plot()
    return philadelphia_neighborhoods
    
def load_csv_convert_to_gpd(csv) -> str:
    incidents_df = pd.read_csv(csv)
    incidents_geo_df = gpd.GeoDataFrame(
    incidents_df, 
    geometry=gpd.points_from_xy(incidents_df.lng, incidents_df.lat,crs='EPSG:4326')
    )
    return incidents_geo_df

def load_gpd_and_correct_crs():
    philadelphia_neighborhoods = load_shp_file('AssignmentData/Neighborhoods_Philadelphia/Neighborhoods_Philadelphia.shp')
    incidents_geo_df = load_csv_convert_to_gpd('AssignmentData/incidents.csv')
    incidents_geo_df = incidents_geo_df[(incidents_geo_df.lat > 38)]
    incidents_geo_df.plot(markersize=0.2)
    philadelphia_neighborhoods.crs
    incidents_geo_df.crs
    incidents_projected_geo_df = incidents_geo_df.to_crs(epsg=2272)
    incidents_projected_geo_df.crs
    fig, ax = plt.subplots()
    incidents_projected_geo_df.plot(ax=ax)
    
def load_and_process_data():
    load_shp_file('AssignmentData/Neighborhoods_Philadelphia/Neighborhoods_Philadelphia.shp')
    load_csv_convert_to_gpd('AssignmentData/incidents.csv')
    load_gpd_and_correct_crs()
    
if __name__ == '__main__':
    load_and_process_data()

