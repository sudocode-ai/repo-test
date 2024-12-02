
from ... import package_name as some_package

def test_unknown():
    some_class = some_package.CoreClass()
    assert some_class.do_something() == 6
