#!/usr/bin/python3

import os
import unittest
from models import storage
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Unit tests for the Review class.
    """

    def setUp(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_place_id_type(self):
        review_model = Review()
        self.assertIsInstance(review_model.place_id, str)

    def test_user_id_type(self):
        review_model = Review()
        self.assertIsInstance(review_model.user_id, str)

    def test_text_type(self):
        review_model = Review()
        self.assertIsInstance(review_model.text, str)


if __name__ == '__main__':
    unittest.main()
