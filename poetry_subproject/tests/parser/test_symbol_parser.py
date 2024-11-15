from poetry_subproject.parser.symbol_parser import SymbolParser  # Assuming the previous code is in symbol_parser.py

def test_symbol_parser():
    parser = SymbolParser()
    
    # Test code with various symbols
    test_code = """
class TestClass:
    def __init__(self):
        self.x = 1
    
    def test_method(self):
        temp = 2
        return temp + self.x

global_var = 42
"""
    
    symbols = parser.extract_symbols(test_code)
    
    # Test class extraction
    assert len(symbols['classes']) == 1
    assert symbols['classes'][0]['name'] == 'TestClass'
    
    # Test function extraction
    assert len(symbols['functions']) == 2
    assert sorted([f['name'] for f in symbols['functions']]) == ['__init__', 'test_method']
    
    # Test variable extraction
    assert len(symbols['variables']) >= 3  # x, temp, global_var
    var_names = [v['name'] for v in symbols['variables']]
    assert 'global_var' in var_names
    assert 'temp' in var_names
    
def test_symbol_parser_base_class():
    parser = SymbolParser()
    assert parser.base_function() == 10

def test_symbol_parser_special_class():
    parser = SymbolParser()
    assert parser.special_function() == 5
    