import os
from unittest import TestCase
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(TestCase):
    def setUp(self):
        self.fs = FileStorage()
        self.b1 = BaseModel()
        self.file_path = "file.json"

    def test_class_attributes(self):
        self.assertIsInstance(self.fs._FileStorage__file_path, str)
        self.assertIsInstance(self.fs._FileStorage__objects, dict)

    def test_new(self):
        self.assertIn(self.b1, self.fs.all().values())

    def test_save(self):
        self.fs.new(self.b1)
        self.fs.save()

        with open(self.file_path, "r") as f:
            read_data = f.read()
        self.assertIn("{}.{}".format(self.b1.__class__.__name__, self.b1.id), read_data)

    def test_reload(self):
        self.fs.save()
        self.fs._FileStorage__objects.clear()
        self.fs.reload()

        self.assertNotEqual(len(self.fs._FileStorage__objects), 0)

    def tearDown(self):
        try:
            os.remove(self.file_path)
        except IOError:
            pass
