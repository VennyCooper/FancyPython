from node import Node 
class BinaryTree:
    def __init__(self, data=None):
        self.root = None if data == None else Node(data)
    
    def insert(self, data):
        pass
    
    def delete(self, data):
        pass
    
    def search(self, data) -> Node:
        pass
    
    def get_tree_depth(self) -> int:
        return self.get_depth_from_node(self.root)

    def get_depth_from_node(self, start_node: Node) -> int:
        if start_node is None:
            return 0
        left_child_depth = self.get_depth_from_node(start_node.left)
        right_child_depth = self.get_depth_from_node(start_node.right)
        return max(left_child_depth + 1, right_child_depth + 1)

    def preorder_traversal(self, root_node: Node):
        if root_node == None:
            return
        root_node.print_node()
        self.preorder_traversal(root_node.left)
        self.preorder_traversal(root_node.right)
    
    def postorder_traversal(self, root_node: Node):
        if root_node == None:
            return
        self.postorder_traversal(root_node.left)
        self.postorder_traversal(root_node.right)
        root_node.print_node()

    def inorder_traversal(self, root_node: Node):
        if root_node == None:
            return
        self.inorder_traversal(root_node.left)
        root_node.print_node()
        self.inorder_traversal(root_node.right)

    def get_node_level(self, root_node=None) -> int:
        pass


    def get_nodes_at_each_level(self, root_node=None) -> list:
        pass

    def print_tree(self):
        pass