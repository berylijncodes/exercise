from unittest import TestCase
from unittest.mock import Mock

from geolocator.service import Service

class TestService(TestCase):
    def setUp(self):
        self.database = Mock()
        self.geolocation_client = Mock()
        self.service = Service(self.database, self.geolocation_client)

    def test_can_retrieve_cities_from_db(self):
        longitude = 123
        latitude = 456
        name = "London"
        country = "GB"

        self.database.get.return_value = [
            {
                "latitude": latitude,
                "longitude": longitude,
                "name": name,
                "country": country
            }
        ]

        result = self.service.retrieve_cities(latitude, longitude)

        self.assertEqual(result, [
            {
                "latitude": latitude,
                "longitude": longitude,
                "name": name,
                "country": country
            }
        ])

        self.database.get.assert_called_once_with(latitude, longitude)

        self.geolocation_client.get.assert_not_called()

        self.database.write.assert_not_called()

    def test_can_retrieve_cities_from_api_and_write_to_db(self):
        longitude = 123
        latitude = 456
        name = "London"
        country = "GB"

        self.database.get.return_value = []
        self.geolocation_client.get.return_value = [
            {
                "latitude": latitude,
                "longitude": longitude,
                "name": name,
                "country": country
            }
        ]

        result = self.service.retrieve_cities(latitude, longitude)

        self.assertEqual(result, [
            {
                "latitude": latitude,
                "longitude": longitude,
                "name": name,
                "country": country
            }
        ])

        self.database.get.assert_called_once_with(latitude, longitude)

        self.geolocation_client.get.assert_called_once_with(latitude, longitude)

        self.database.write.assert_called_once_with(latitude, longitude, name, country)
