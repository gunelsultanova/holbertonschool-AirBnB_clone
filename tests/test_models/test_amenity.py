#!/usr/bin/python3

import os
import unittest

from models import storage
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Unit tests for the Amenity class.
    """

    def setUp(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_name_type(self):
        amenity_model = Amenity()
        self.assertIsInstance(amenity_model.name, str)


if __name__ == '__main__':
    unittest.main()
