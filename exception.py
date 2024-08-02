
class CustomException(Exception):
    pass

class ItemError(CustomException):
    def __init__(self, message="Invalid item"):
        super().__init__(message)

class LessQuantityError(CustomException):
    def __init__(self, message="Insufficient quantity."):
        super().__init__(message)
