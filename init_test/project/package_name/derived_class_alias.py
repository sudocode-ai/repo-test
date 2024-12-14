from project.nested_package_twice.base_class import BaseClass as BaseClassAlias

class ExternalImportBaseClassAlias(BaseClassAlias):
    def __init__(self):
        print("do nothing")
        pass
        
    def get_number(self):
        number = self.base_function()
        return number