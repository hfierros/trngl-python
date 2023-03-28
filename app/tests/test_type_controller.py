import flask_unittest
from app.main import create_app
from app.main.service.type_service import get_triangle_type
from app import blueprint


class TestTypeController(flask_unittest.AppTestCase):
    
    def create_app(self):
        app = create_app('test')
        app.register_blueprint(blueprint)
        app.app_context().push()
        return app
    
    def test_get_triangle_type(self, app):
        client = app.test_client()
        triangle = {
            "sideA": 1,
            "sideB": 1,
            "sideC": 1
        }
        response = client.post('/type/', json=triangle)
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response.json, {"type": "EQUILATERAL"})
                         