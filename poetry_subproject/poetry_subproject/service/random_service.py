from poetry_subproject.parser.symbol_parser import (
    SymbolParser,
    random_function,
)
from typing import Dict
import pydantic

GLOBAL_VAR = "hello"
print("goodbye")

class ClassToTest():
    def __init__(self):
        self.parser = SymbolParser()
        
    def count_symbols(self, input_to_test: str) -> Dict[str, int]:
        symbols = self.parser.extract_symbols(input_to_test)
        return {
            'class_count': len(symbols['classes']),
            'function_count': len(symbols['functions']),
            'variable_count': len(symbols['variables'])
        }

class RandomClass(pydantic.BaseModel):
    random_str: str

def count_symbols(input_to_test: str) -> Dict[str, int]:
    """
    Count the number of each type of symbol in the input code.
    
    Args:
        input_to_test: String containing Python code
        
    Returns:
        Dictionary with counts of classes, functions, and variables
    """
    parser = SymbolParser()
    symbols = parser.extract_symbols(input_to_test)
    val = random_function()
    print(val)
    return {
        'class_count': len(symbols['classes']),
        'function_count': len(symbols['functions']),
        'variable_count': len(symbols['variables']),
    }
    