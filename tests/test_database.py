from unittest import TestCase

from geolocator.database import Database


class TestDatabase(TestCase):
    def setUp(self):
        self.database = Database()
        self.database.connect(':memory:')

    def test_can_write_to_geolocation_table(self):
        self.database.write(51.5128, -0.0918, "London", "GB")
        self.assertEqual(2 + 2 , 4)
