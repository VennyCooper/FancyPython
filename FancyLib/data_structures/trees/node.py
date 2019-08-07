class Node:
    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
   
    def print_node(self):
        left_data = None if self.left is None else self.left.data
        right_data = None if self.right is None else self.right.data
        parent_data = None if self.parent is None else self.parent.data
        print(f'[Node] Value({str(type(self.data))}): {str(self.data)} | L: {str(left_data)}, R: {str(right_data)}, P: {str(parent_data)}')