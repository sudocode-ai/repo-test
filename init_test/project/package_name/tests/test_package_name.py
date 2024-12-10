from ... import package_name as some_package

def test_unknown():
    result = some_package.CoreClass().do_something()
    assert result == 6

def test_second_package():
    result = some_package.nested_package.OtherCoreClass().do_something()
    assert result == 6
