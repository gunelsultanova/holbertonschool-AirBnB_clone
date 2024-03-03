#!/usr/bin/python3

import os
import unittest
from models import storage
from models.state import State


class TestState(unittest.TestCase):
    """
    Unit tests for the State class.
    """

    def setUp(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_name_type(self):
        state_model = State()
        self.assertIsInstance(state_model.name, str)


if __name__ == '__main__':
    unittest.main()
