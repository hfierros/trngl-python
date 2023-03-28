from flask import request
from flask_restx import Resource
from ..dto.triangle_request_dto import TriangleDto
from ..service.type_service import get_triangle_type

api = TriangleDto.api
_triangle = TriangleDto

@api.route('/')
class TriangleType(Resource):
    @api.response(200, 'Triangle type calculated')
    @api.doc('Get triangle type')
    @api.expect(_triangle, validate=True)
    def post(self):
        triangle = request.json
        return get_triangle_type(triangle)

