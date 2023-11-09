from unittest import TestCase

import responses

from geolocator.client import Client


class TestClient(TestCase):
    def setUp(self):
        self.client = Client("TEST_API_KEY")

    @responses.activate
    def test_gets_the_geolocation_information(self):
        expected_response = [
            {
                "lat": 51.5128,
                "lon": -0.0918,
                "name": "London",
                "country": "GB"
            },
        ]

        responses.add(responses.GET, "http://api.openweathermap.org/geo/1.0/reverse",
                      json=expected_response, status=200)

        response = self.client.get(51.5128, -0.0918)

        self.assertEqual(len(response), len(expected_response))
        for i in range(len(response)):
            self.assertEqual(response[i]["latitude"], expected_response[i]["lat"])
            self.assertEqual(response[i]["longitude"], expected_response[i]["lon"])
            self.assertEqual(response[i]["name"], expected_response[i]["name"])
            self.assertEqual(response[i]["country"], expected_response[i]["country"])

        self.assertEqual(responses.calls[0].request.url, "http://api.openweathermap.org/geo/1.0/reverse?lat=51.5128&lon=-0.0918&limit=10&appid=TEST_API_KEY")

    @responses.activate
    def test_returns_empty_list_when_no_cities_are_found(self):
        responses.add(responses.GET, "http://api.openweathermap.org/geo/1.0/reverse",
                      json=[], status=200)
        
        response = self.client.get(51.5128, -0.0918)

        self.assertEqual(response, [])

    def test_invalid_latitude_and_longitude(self):
        with self.assertRaises(Exception):
            self.client.get(1000, 2000)
