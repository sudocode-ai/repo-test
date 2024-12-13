from ... import package_name as some_package

def test_aliased_package_import():
    result = some_package.CoreClass().do_something()
    assert result == 6
    