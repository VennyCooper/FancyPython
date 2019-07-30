class Node:
   def __init__(self, data, left=None, right=None):
      self.data = data
      self.left = left
      self.right = right
   
   def print_node(self):
      print(f'[Node] Value({str(type(self.data))}): {str(self.data)} | L_Child: {str(left)}, R_Child: {str(right)}')