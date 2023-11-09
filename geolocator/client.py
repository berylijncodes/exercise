import requests
from typing import List

from .models import City


class Client:
    limit = 10

    def __init__(self, api_key):
        self._api_key = api_key

    def _serialize(self, raw_data: dict) -> City:
       return [
        {
            "latitude": city["lat"],
            "longitude": city["lon"],
            "name": city["name"],
            "country": city["country"]
        } for city in raw_data
       ]

    def get(self, latitude, longitude) -> List[City]:
        url = f"http://api.openweathermap.org/geo/1.0/reverse?lat={latitude}&lon={longitude}&limit={self.limit}&appid={self._api_key}"

        print("Making API request.", url)

        response = requests.get(url)

        if response.status_code != 200:
            raise Exception("Error: Api request unsuccessful.")

        raw_data = response.json()

        return self._serialize(raw_data)
