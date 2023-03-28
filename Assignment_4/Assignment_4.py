#%%
from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim
import pandas as pd
import plotly_express as px


# generate locator

locator = Nominatim(user_agent="myGeocoder")
address = "Jodenbreestraat 4, Netherlands"
location = locator.geocode(address)
location
location.point
location.latitude
location.longitude

# load dataframe

df = pd.read_csv("AssignmentData/PPR_Swimming_Pools.csv")
df.head()

# generate geocode

df["ADDRESS"] = df['ADDRESS_911'] + " Philadelphia, USA"
geocode = RateLimiter(locator.geocode, min_delay_seconds=1)
df['location'] = df['ADDRESS'].apply(geocode)
df['point'] = df['location'].apply(lambda loc: tuple(loc.point) if loc else None)
df.head()
df[['latitude', 'longitude', 'altitude']] = pd.DataFrame(df['point'].tolist(), index=df.index)
df.head()
fig = px.scatter_mapbox(
    df,   
    lat="latitude", 
    lon="longitude", 
    mapbox_style="carto-darkmatter",
    zoom=5)
fig.show()

