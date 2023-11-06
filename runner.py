import os
from dotenv import load_dotenv
from prettytable import PrettyTable

from geolocator.client import Client
from geolocator.database import Database
from geolocator.user_interface import UserInterface
from geolocator.service import Service

load_dotenv()

db_path = os.path.join(os.path.dirname(__file__), "db", "database.db")
database = Database()
database.connect(db_path)

geolocator_api_key = os.environ.get("GEOLOCATOR_API_KEY")

client = Client(geolocator_api_key)
ui = UserInterface()

service = Service(database, client)

# wire everything up below:
print("Welcome to Geolocator")

# get location from user
latitude, longitude, = ui.get_location()
print("Retrieving cities and country codes for: ", latitude, longitude,)

# retrive database information for the location
cities = service.retrieve_cities(latitude, longitude)

# render data to user in a table form
table = PrettyTable()
table.field_names = ["Latitude", "Longitude", "City", "Country Code"]

for city in cities:
    table.add_row([city["latitude"], city["longitude"], city["name"], city["country"]])

print(table)
