from flask_restx import Namespace, fields


class TriangleDto:
    api = Namespace('triangle', description = 'Triangle request object')
    triangle = api.model('triangle' , {
        'sideA' : fields.Integer(required=True, description='Lado a', min=1), 
        'sideB' : fields.Integer(required=True, description='Lado b', min=1),
        'sideC' : fields.Integer(required=True, description='Lado c', min=1)
        })
