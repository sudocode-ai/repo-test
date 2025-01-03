import project.package_name

def test_package_exported_class():
    # Tests CoreClass imported through package __init__.py
    number = project.package_name.CoreClass()
    assert number == 5
    
def test_package_exported_nested_class():
    # Tests OtherCoreClass imported through package __init__.py
    number = project.package_name.OtherCoreClass()
    assert number == 5
    
def test_package_exported_function():
    # Tests package_function imported through package __init__.py
    number = project.package_name.package_function()
    assert number == 5
    
def test_package_exported_nested_class_method_call():
    # Tests OtherCoreClass imported through package __init__.py
    number = project.package_name.OtherCoreClass().do_something()
    assert number == 5