from poetry_subproject.service.random_service import ClassToTest, count_symbols
import pytest

@pytest.fixture
def sample_code():
    return """
class SampleClass:
    def __init__(self):
        self.instance_var = 123
        
    def sample_method(self):
        local_var = 456
        return local_var

global_variable = 789

class AnotherClass:
    pass
"""

def test_direct_counter_usage(sample_code):
    # Test the direct function
    counts = count_symbols(sample_code)
    
    assert counts['class_count'] == 2  # SampleClass and AnotherClass
    assert counts['function_count'] == 2  # __init__ and sample_method
    assert counts['variable_count'] == 3  # instance_var, local_var, global_variable

def test_class_counter_usage(sample_code):
    # Test the class-based usage
    counter = ClassToTest()
    counts = counter.count_symbols(sample_code)
    
    assert counts['class_count'] == 2
    assert counts['function_count'] == 2
    assert counts['variable_count'] == 3

def test_counter_identical_results(sample_code):
    # Test that both methods produce identical results
    direct_results = count_symbols(sample_code)
    class_results = ClassToTest().count_symbols(sample_code)
    
    assert direct_results == class_results

def test_empty_code():
    empty_code = ""
    counts = count_symbols(empty_code)
    
    assert counts['class_count'] == 0
    assert counts['function_count'] == 0
    assert counts['variable_count'] == 0

def test_complex_code():
    complex_code = """
class A:
    def __init__(self):
        self.x = 1
        self.y = 2
        
    def method1(self): pass
    def method2(self): pass

class B:
    z = 3
    def method3(self): pass

global_var1 = 4
global_var2 = 5
"""
    counts = count_symbols(complex_code)
    
    assert counts['class_count'] == 2  # A and B
    assert counts['function_count'] == 4  # __init__, method1, method2, method3
    assert counts['variable_count'] == 5  # x, y, z, global_var1, global_var2