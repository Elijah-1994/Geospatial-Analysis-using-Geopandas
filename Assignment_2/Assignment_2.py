import contextily as ctx
import geopandas as gpd
import matplotlib.pyplot as plt


def load_shp_files(shapefile):
    geo_data_frames = []
    for shapefiles in shapefile:
        geo_data_frame  = gpd.read_file(shapefiles)
        geo_data_frames.append(geo_data_frame)
    return (geo_data_frames)

def load_shp_files_and_plot_maps():
    philadelphia_neighborhood_gpd = load_shp_files(['AssignmentData/Neighborhoods_Philadelphia.shp','AssignmentData/swimming_pools.shp'])[0]
    swimming_pools_gpd = load_shp_files(['AssignmentData/Neighborhoods_Philadelphia.shp','AssignmentData/swimming_pools.shp'])[1]
    swimming_pool_projected_gpd = swimming_pools_gpd.to_crs(epsg=2272)
    fig, ax = plt.subplots(1,1,  figsize=(12,10))
    philadelphia_neighborhood_gpd.plot(ax=ax, color="gray", linewidth=0.3, alpha=0.5);
    swimming_pool_projected_gpd.plot(ax= ax,
                    color="black",
                    alpha=0.7)
    plt.title('Swimming pools in philadelphia', fontsize=40, fontname="Palatino Linotype", color="grey")
    ax.axis("off")
    plt.axis('equal')
    plt.show()

def overlay_data_onto_basemap():
    swimming_pools_gpd = load_shp_files(['AssignmentData/Neighborhoods_Philadelphia.shp','AssignmentData/swimming_pools.shp'])[1]
    ctx.providers.keys()
    fig, ax = plt.subplots(figsize=(12, 10))
    swimming_pools_gpd.to_crs(epsg=3857).plot(ax = ax,
            figsize=(12,12),
            markersize=40,
            color="black",
            edgecolor="white",
            alpha=0.8,
            marker="o"
            );
    ctx.add_basemap(ax, url=ctx.providers.Stamen.TonerLite);

def create_choropleth_map(geojson):
    neighbourhood_crimes = gpd.read_file(geojson)
    neighbourhood_crimes.columns
    neighbourhood_crimes.plot(column='Counts', figsize=(12,10));
    neighbourhood_crimes["Counts"] = (neighbourhood_crimes['Counts']/neighbourhood_crimes['Shape_Area'])*100
    neighbourhood_crimes["Counts"]
    fig, ax = plt.subplots(figsize=(12,10))
    neighbourhood_crimes.plot(column='Counts', cmap="Blues", scheme="quantiles", k=6, ax=ax, legend=True);

def load_data_and_create_maps():
    load_shp_files(['AssignmentData/Neighborhoods_Philadelphia.shp','AssignmentData/swimming_pools.shp'])
    load_shp_files_and_plot_maps()
    overlay_data_onto_basemap()
    create_choropleth_map('AssignmentData/neighbourhood_crimes.Geojson')

if __name__ == '__main__':
    load_data_and_create_maps()

    
