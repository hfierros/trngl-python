from flask_restx import Api
from flask import Blueprint

from .main.controller.type_controller import api as triangle_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint, title='TRIANGLE Example', version='1.0', description='QA class triangle python example')

api.add_namespace(triangle_ns, path='/type')
