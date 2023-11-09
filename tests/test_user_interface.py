from io import StringIO
import sys
from unittest import TestCase

from geolocator.user_interface import UserInterface

class TestUserInterface(TestCase):
    def setUp(self):
        self.ui = UserInterface()

    def test_get_location(self):
        input_data = "51.5128,-0.0918\n"
        expected_latitude = 51.5128
        expected_longitude = -0.0918

        original_stdin = sys.stdin

        sys.stdin = StringIO(input_data)

        latitude, longitude = self.ui.get_location()

        sys.stdin = original_stdin

        self.assertEqual(latitude, expected_latitude)
        self.assertEqual(longitude, expected_longitude)
