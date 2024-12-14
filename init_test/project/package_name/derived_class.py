from project.nested_package import base_class

class DerivedExternalBaseClass(base_class.BaseClass):
    def __init__(self):
        print("do nothing")
        pass
        
    def get_number(self):
        number = self.base_function()
        return number
    
class InternalBaseClass:
    field: str
    def __init__():
        return
    
    def base_function():
        print("Hello world")
        var = 5
        return var + 1
    
    
class DerivedInternalBaseClass(InternalBaseClass):
    def __init__(self):
        print("do nothing")
        pass
        
    def get_number(self):
        number = self.base_function()
        return number
    
    