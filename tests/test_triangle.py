import unittest
import json
from flasky import app


class TriangleTypeTest(unittest.TestCase):

    def setUp(self):
        # Configura el cliente de pruebas de Flask
        self.client = app.test_client()

    def post_triangle(self, a, b, c):
        """Helper para hacer POST a /type."""
        body = {"sideA": a, "sideB": b, "sideC": c}
        return self.client.post(
            "/type", data=json.dumps(body), content_type="application/json"
        )

    # -------------------------
    # PRUEBAS PARA TRIÁNGULOS VÁLIDOS
    # -------------------------

    def test_equilateral(self):
        resp = self.post_triangle(3, 3, 3)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json().get("type"), "EQUILATERAL")

    def test_isosceles(self):
        resp = self.post_triangle(4, 4, 5)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json().get("type"), "ISOSCELES")

    def test_scalene(self):
        resp = self.post_triangle(3, 4, 5)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json().get("type"), "SCALENE")

    # -------------------------
    # PRUEBAS PARA DATOS INVÁLIDOS
    # -------------------------

    def test_invalid_negative_values(self):
        resp = self.post_triangle(-1, 3, 3)
        self.assertEqual(resp.status_code, 400)

    def test_invalid_zero_values(self):
        resp = self.post_triangle(0, 5, 5)
        self.assertEqual(resp.status_code, 400)

    def test_not_a_triangle(self):
        # regla: un lado no puede ser mayor o igual a la suma de los otros dos
        resp = self.post_triangle(1, 2, 10)
        self.assertEqual(resp.status_code, 400)

    def test_missing_field(self):
        # envía un json incompleto
        resp = self.client.post(
            "/type", data=json.dumps({"sideA": 1}), content_type="application/json"
        )
        self.assertEqual(resp.status_code, 400)


if __name__ == "__main__":
    unittest.main()
