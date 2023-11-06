from io import StringIO
import sys
from unittest import TestCase

from geolocator.user_interface import UserInterface


class TestUserInterface(TestCase):
    def setUp(self):
        self.ui = UserInterface()

        self.output = StringIO()
        sys.stdout = self.output

    def tearDown(self):
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__

    def test_prints_the_answer(self):
        sys.stdin = StringIO("The Answer")
        self.ui.hello()
        self.assertIn("The Answer", self.output.getvalue())
