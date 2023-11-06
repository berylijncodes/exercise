import os
from dotenv import load_dotenv

from geolocator.client import Client
from geolocator.database import Database
from geolocator.user_interface import UserInterface

load_dotenv()

db_path = os.path.join(os.path.dirname(__file__), "db", "database.db")
database = Database()
database.connect(db_path)

geolocator_api_key = os.environ.get("GEOLOCATOR_API_KEY")

client = Client(geolocator_api_key)
ui = UserInterface()

# wire everything up below:
print("Welcome to Geolocator")
