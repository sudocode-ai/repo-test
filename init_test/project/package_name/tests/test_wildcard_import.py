from project.package_name import *

def test_unknown():
    number = core.package_function()
    assert number == 5

def test_class():
    number = CoreClass()
    assert number == 5
