from ...package_name import DerivedInternalBaseClass, DerivedExternalBaseClass

def test_derived_internal_class():
    number = DerivedInternalBaseClass()
    assert number.get_number() == 5
    
def test_derived_external_package_class():
    number = DerivedExternalBaseClass()
    assert number.get_number() == 5
    