import requests


class Client:
    limit = 10

    def __init__(self, api_key):
        self._api_key = api_key

    def get(self, latitude, longitude,):
        url = f"http://api.openweathermap.org/geo/1.0/reverse?lat={latitude}&lon={longitude}&limit={self.limit}&appid={self._api_key}"

        print("Making API request.", url)

        response = requests.get(url)

        if response.status_code != 200:
            raise Exception("Error: Api request unsuccessful.")

        raw_data = response.json()

        return raw_data
