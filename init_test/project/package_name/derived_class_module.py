import project.nested_package_twice.base_class

class ExternalImportBaseClass(project.nested_package_twice.base_class.BaseClass):
    def __init__(self):
        print("do nothing")
        pass
        
    def get_number(self):
        number = self.base_function()
        return number
    