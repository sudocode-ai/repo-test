from project.package_name import core

def test_module_import():
    number = core.package_function()
    assert number == 5
