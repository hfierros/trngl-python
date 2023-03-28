import unittest
from app.main.service.type_service import get_triangle_type

class TestTypeService(unittest.TestCase):
    def test_get_triangle_type(self):
        triangle = {
            "sideA": 1,
            "sideB": 1,
            "sideC": 1
        }
        self.assertEqual(get_triangle_type(triangle), ({"type": "EQUILATERAL"}, 200))
        