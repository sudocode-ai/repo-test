from ...package_name import core as some_package
def test_unknown():
    number = some_package.package_function()
    assert number == 5