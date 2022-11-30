from modis_tools.auth import ModisSession
from modis_tools.resources import CollectionApi, GranuleApi
from modis_tools.granule_handler import GranuleHandler

username = ""  # Update this line
password = ""  # Update this line
# Authenticate a session
session = ModisSession(username=username, password=password)

# Query the MODIS catalog for collections
collection_client = CollectionApi(session=session)
collections = collection_client.query(short_name="MOD13A1", version="006")

# Query the selected collection for granules
granule_client = GranuleApi.from_collection(collections[0], session=session)

# Filter the selected granules via spatial and temporal parameters
nigeria_bbox = [2.1448863675, 4.002583177, 15.289420717, 14.275061098]
nigeria_granules = granule_client.query(start_date="2019-01-01", end_date="2019-01-01", bounding_box=nigeria_bbox)

# Download the granules
GranuleHandler.download_from_granules(nigeria_granules, session,path="C:/Users/DELL/PycharmProjects/pythonProject4/images")