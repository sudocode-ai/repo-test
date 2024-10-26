import importlib
from tree_sitter import Language, Parser
from typing import Dict, List

class SymbolParser:
    def __init__(self):
        self.parser = Parser()
        
        language_module = importlib.import_module("tree_sitter_python")
        language_func = getattr(language_module, "language")
        ts_language = Language(language_func())
        self.parser = Parser(ts_language)
    
    def extract_symbols(self, code: str) -> Dict[str, List[Dict]]:
        """Extract symbols (functions, classes, variables) from code."""
        tree = self.parser.parse(bytes(code, 'utf8'))
        root_node = tree.root_node
        
        symbols = {
            'functions': [],
            'classes': [],
            'variables': []
        }
        
        def get_node_text(node):
            start_byte = node.start_byte
            end_byte = node.end_byte
            return code[start_byte:end_byte]
        
        def traverse_node(node):
            if node.type == 'function_definition':
                name_node = node.children[1] if len(node.children) > 1 else None
                if name_node:
                    symbols['functions'].append({
                        'name': get_node_text(name_node),
                        'start_line': node.start_point[0] + 1,
                        'end_line': node.end_point[0] + 1
                    })
            
            elif node.type == 'class_definition':
                name_node = node.children[1] if len(node.children) > 1 else None
                if name_node:
                    symbols['classes'].append({
                        'name': get_node_text(name_node),
                        'start_line': node.start_point[0] + 1,
                        'end_line': node.end_point[0] + 1
                    })
            
            # Handle both regular assignments and attribute assignments
            elif node.type in ('assignment', 'expression_statement'):
                for child in node.children:
                    # Regular variable assignments
                    if child.type == 'identifier':
                        symbols['variables'].append({
                            'name': get_node_text(child),
                            'line': child.start_point[0] + 1
                        })
                    # Instance variable assignments (self.x)
                    elif child.type == 'attribute' and child.children[0].type == 'identifier':
                        attr_name = get_node_text(child.children[2])  # Get the attribute name
                        symbols['variables'].append({
                            'name': attr_name,
                            'line': child.start_point[0] + 1
                        })
            
            for child in node.children:
                traverse_node(child)
        
        traverse_node(root_node)
        return symbols
    
    def parse_file(self, file_path: str) -> Dict[str, List[Dict]]:
        """Parse a file and extract its symbols."""
        with open(file_path, 'r') as f:
            code = f.read()
        return self.extract_symbols(code)
    
def random_function():
    return 10