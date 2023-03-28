#%%
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx

pn = gpd.read_file('AssignmentData/Neighborhoods_Philadelphia.shp')
pn.head(5)
swimming_pool_gdf = gpd.read_file('AssignmentData/swimming_pools.shp')
#swimming_pool_gdf.head(5)
#swimming_pool_gdf.plot()
#pn.plot()
swimming_pool_projected_gdf = swimming_pool_gdf.to_crs(epsg=2272)
sp2 = swimming_pool_projected_gdf.crs
# fig, ax = plt.subplots(1,1,  figsize=(12,10))
# pn.plot(ax=ax, color='#C05A3C', linewidth=0.3, alpha=0.5);
# swimming_pool_projected_gdf.plot(ax= ax,
#                 color='#F1ECEB',
#                 alpha=0.7)
# plt.title('Mälmo Neighbourhoods', fontsize=40, fontname="Palatino Linotype", color="grey")
# ax.axis("off")
# plt.axis('equal')
# plt.show()

## basemap
# ctx.providers.keys()
# fig, ax = plt.subplots(figsize=(12, 10))
# swimming_pool_projected_gdf.to_crs(epsg=3857).plot(ax = ax,
#                 figsize=(12,12),
#                 markersize=40,
#                color="black",
#                edgecolor="white",
#                alpha=0.8,
#                marker="o"
#             );
# ctx.add_basemap(ax, url=ctx.providers.Stamen.TonerLite);
## choropleth map
crimes = gpd.read_file('AssignmentData/neighbourhood_crimes.Geojson')
crimes.head(5)
crimes.columns
crimes.plot(column='Counts', figsize=(12,10));
crimes["Counts"] = (crimes['Counts']/crimes['Shape_Area'])*100
crimes["Counts"]
fig, ax = plt.subplots(figsize=(12,10))
crimes.plot(column='Counts', cmap="Blues", scheme="quantiles", k=6, ax=ax, legend=True);