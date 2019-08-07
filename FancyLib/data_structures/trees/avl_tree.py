from binary_search_tree import BinarySearchTree
from node import Node

'''
    Methods that keep same as in base class BinarySearchTree:
        1. search(self, data) -> Node
        2. get_nodes_at_each_level(self, root_node=None) -> list
        3. get_node_level(self, data) -> int
        4. get_node_with_min_data(self, root_node=None) -> Node
        5. get_node_with_max_data(self, root_node=None) -> Node
        6. is_tree_empty(self) -> bool
        7. is_node_left_child(self, node: Node) -> bool
        8. replace_node(self, old_node: Node, new_node: Node)
'''
class AvlTree(BinarySearchTree):
    # load a binary search tree and construct an AVL tree based on it
    def __init__(self, bst: BinarySearchTree):
        pass

    def delete(self, data):
        pass

    def insert(self, data):
        pass

    def ll_rotate(self, node) -> Node:
        pass
    
    def lr_rotate(self, node) -> Node:
        pass
    
    def rr_rotate(self, node) -> Node:
        pass

    def rl_rotate(self, node) -> Node:
        pass
    
