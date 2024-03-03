#!/usr/bin/python3

import os
import unittest
from models import storage
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Unit tests for the Place class.
    """

    def setUp(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_city_id_type(self):
        place_model = Place()
        self.assertIsInstance(place_model.city_id, str)

    def test_user_id_type(self):
        place_model = Place()
        self.assertIsInstance(place_model.user_id, str)

    def test_name_type(self):
        place_model = Place()
        self.assertIsInstance(place_model.name, str)

    def test_description_type(self):
        place_model = Place()
        self.assertIsInstance(place_model.description, str)

    def test_number_rooms_type(self):
        place_model = Place()
        self.assertIsInstance(place_model.number_rooms, int)

    def test_number_bathrooms_type(self):
        place_model = Place()
        self.assertIsInstance(place_model.number_bathrooms, int)

    def test_max_guest_type(self):
        place_model = Place()
        self.assertIsInstance(place_model.max_guest, int)

    def test_price_by_night_type(self):
        place_model = Place()
        self.assertIsInstance(place_model.price_by_night, int)

    def test_latitude_type(self):
        place_model = Place()
        self.assertIsInstance(place_model.latitude, float)

    def test_longitude_type(self):
        place_model = Place()
        self.assertIsInstance(place_model.longitude, float)

    def test_amenity_ids_type(self):
        place_model = Place()
        self.assertIsInstance(place_model.amenity_ids, list)


if __name__ == '__main__':
    unittest.main()
