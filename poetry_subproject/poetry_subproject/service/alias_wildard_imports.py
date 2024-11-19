from poetry_subproject.parser.symbol_parser import (
    SymbolParser as RenamedSymbolParser,
    random_function as aliased_function,
)
from poetry_subproject.parser.util import *
from typing import Dict
import pydantic

GLOBAL_VAR = "hello"
print("goodbye")

class AliasedClassToTest():
    def __init__(self):
        self.parser = RenamedSymbolParser()
        
    def count_symbols(self, input_to_test: str) -> Dict[str, int]:
        symbols = self.parser.extract_symbols(input_to_test)
        return {
            'class_count': len(symbols['classes']),
            'function_count': len(symbols['functions']),
            'variable_count': len(symbols['variables'])
        }

class RandomClass(pydantic.BaseModel):
    random_str: str

def count_symbols_aliased(input_to_test: str) -> Dict[str, int]:
    """
    Count the number of each type of symbol in the input code.
    
    Args:
        input_to_test: String containing Python code
        
    Returns:
        Dictionary with counts of classes, functions, and variables
    """
    parser = RenamedSymbolParser()
    symbols = parser.extract_symbols(input_to_test)
    print(aliased_function())
    return {
        'class_count': len(symbols['classes']),
        'function_count': len(symbols['functions']),
        'variable_count': random_function_three(),
    }
    