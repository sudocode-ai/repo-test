from project.package_name.core import CoreClass, package_function

def test_direct_class_call():
    number = CoreClass()
    assert number == 5
    
def test_direct_function_call():
    number = package_function()
    assert number == 5
    
    