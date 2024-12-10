from ...package_name import CoreClass, package_function, OtherCoreClass

def test_package_exported_class():
    # Tests CoreClass imported through package __init__.py
    number = CoreClass()
    assert number == 5
    
def test_package_exported_nested_class():
    # Tests OtherCoreClass imported through package __init__.py
    number = OtherCoreClass()
    assert number == 5
    
def test_package_exported_function():
    # Tests package_function imported through package __init__.py
    number = package_function()
    assert number == 5