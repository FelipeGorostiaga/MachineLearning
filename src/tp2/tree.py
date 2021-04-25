from enum import Enum

NodeType = Enum('NodeType', 'attr val leaf')

class Tree:
    class Node:
        def __init__(self, node_type, value=None):
            self.children = []
            self.value = value
            self.node_type = node_type
        
        def __str__(self):
            curr = f'\n{self.value}\n'
            for child in self.children:
                curr += str(child)
            return curr
        
        def add_child(self, node_type, child_value):
            child = Tree.Node(node_type, child_value)
            self.children.append(child)
            return child
    
    def __init__(self, root_value=None):
        self.root = Tree.Node(NodeType.attr, root_value)
    
    def __str__(self):
        return str(self.root)
