from node import Node 
class Tree:
    def __init__(self, data):
        self.root = Node(data)
    
    def insert(self, data):
        pass
    
    def delete(self, data):
        pass
    
    def search(self, data) -> Node:
        pass
    
    def preorder_traversal(self, root_node):
        if root_node == None:
            return
        root_node.print_node()
        self.preorder_traversal(root_node.left)
        self.preorder_traversal(root_node.right)
    
    def postorder_traversal(self, root_node):
        if root_node == None:
            return
        self.postorder_traversal(root_node.left)
        self.postorder_traversal(root_node.right)
        root_node.print_node()

    def inorder_traversal(self, root_node):
        if root_node == None:
            return
        self.inorder_traversal(root_node.left)
        root_node.print_node()
        self.inorder_traversal(root_node.right)

    def print_tree(self):
        pass