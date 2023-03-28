from ..util.triangle_util import is_valid

def get_triangle_type(triangle):

    if is_valid(triangle): 
        if triangle['sideA'] == triangle['sideB'] and triangle['sideB'] == triangle['sideC'] : 
            response_object = {
                    'type' : 'EQUILATERAL'
                    }
            return response_object, 200
        elif triangle['sideA'] != triangle['sideB'] and triangle['sideB'] == triangle['sideC'] :
            response_object = {
                    'type' : 'SCALENE'
                    }
            return response_object, 200
        response_object = {
                'type' : 'ISOSCELES'
                }
        return response_object, 200
    else :
        response_object = {
                'error' : 'Invalid triangle'
                }
        return response_object, 400
