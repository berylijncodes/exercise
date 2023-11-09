from unittest import TestCase

from geolocator.database import Database


class TestDatabase(TestCase):
    def setUp(self):
        self.database = Database()
        self.database.connect(':memory:')

    def test_can_write_to_geolocation_table(self):
        longitude = 123
        latitude = 456
        city = "London"
        country = "GB"

        self.database.write(latitude, longitude, city, country)

        cursor = self.database.connection.cursor()
        cursor.execute(
            """
            SELECT latitude, longitude, city, country_code
            FROM geolocation
            WHERE latitude = ? AND longitude = ?;
            """,
            (latitude, longitude)
        )

        row = cursor.fetchone()

        self.assertEqual(row[0], latitude)
        self.assertEqual(row[1], longitude)
        self.assertEqual(row[2], city)
        self.assertEqual(row[3], country)
        