class Tree:
    class Node:
        def __init__(self, value=None):
            self.children = []
            self.value = value
        
        def __str__(self):
            curr = f'\n{self.value}\n'
            for child in self.children:
                curr += str(child)
            return curr
        
        def add_child(self, child_value):
            child = Tree.Node(child_value)
            self.children.append(child)
            return child
    
    def __init__(self, root_value=None):
        self.root = Tree.Node(root_value)
    
    def __str__(self):
        return str(self.root)
