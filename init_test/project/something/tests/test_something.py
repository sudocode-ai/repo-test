
from ... import something as some

def test_unknown():
    some_class = some.CoreClass()
    assert some_class.do_something() == 6
