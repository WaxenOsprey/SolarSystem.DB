import unittest
from models.visit import Visit


class TestVisit(unittest.TestCase):

    def setUp(self):
        self.visit1 = Visit("Paul", "Mars")


    def test_mark_discovered(self):
        self.visit1.mark_discovered()
        self.assertEqual(True, self.visit1.discovered)
