
def is_valid(triangle):
    if (triangle['sideA'] + triangle['sideB'] > triangle['sideC'] 
        and triangle['sideA'] + triangle['sideC'] > triangle['sideB'] 
        and triangle['sideB'] + triangle['sideC'] > triangle['sideA']):
        return True
    return False 
