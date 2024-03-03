#!/usr/bin/python3

import os
import unittest
from models import storage
from models.city import City


class TestCity(unittest.TestCase):
    """
    Unit tests for the City class.
    """

    def setUp(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_state_id_type(self):
        city_model = City()
        self.assertIsInstance(city_model.state_id, str)

    def test_name_type(self):
        city_model = City()
        self.assertIsInstance(city_model.name, str)


if __name__ == '__main__':
    unittest.main()
