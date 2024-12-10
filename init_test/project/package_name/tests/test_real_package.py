from ...package_name import CoreClass, package_function, OtherCoreClass

def test_class_call():
    number = CoreClass()
    assert number == 5
    
def test_nested_class_call():
    number = OtherCoreClass()
    assert number == 5
    
def test_function_call():
    number = package_function()
    assert number == 5