#%%
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

countries = gpd.read_file('data/countries.shp')
countries.head(6)
conflicts = gpd.read_file("data/acled2019.shp", rows=500)
conflicts.head()
country_shapes = countries[['geometry','NAME']]
country_shapes.head(5)
country_names = countries[['NAME', 'POP_EST']]
countries_gdf_merged = country_shapes.merge(country_names, on='NAME', how='left')
countries_gdf_merged .head()
country_df_merged = country_names.merge(country_shapes, on='NAME', how='left')
country_df_merged.head()
conflict_gdf = conflicts[['event_id_c', 'event_date','fatalities', 'geometry']]
conflicts_in_countries = gpd.sjoin(conflict_gdf, country_shapes, how="inner", op='within')
conflicts_in_countries.sample(10)