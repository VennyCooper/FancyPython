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

    # check if the current tree or a given subtree is an AVL tree
    def check_balance(self, root_node=None) -> bool:
        root_node = self.root if root_node is None else root_node
        return abs(self.get_depth_from_node(root_node.left) - self.get_depth_from_node(self.root.right)) <= 1

    def delete(self, data):
        pass

    def insert(self, data):
        pass

    # case: right right
    # left rotate 10
    #         10 (node)               15
    #        /  \         ->         /  \
    #       7   15                  10  30
    #          /  \                /  \
    #         12  30     n        7   12
    def left_rotate(self, node) -> Node:
        r = node.right
        rl = r.left
        r.left = node
        node.right = rl
        rl.parent = node
        r.parent = node.parent
        node.parent = r

    # case: left left
    # right rotate 10
    #         10 (node)              8
    #        /  \         ->        / \
    #       8   15                 5  10
    #      / \                       /  \
    #     5   9                     9   15
    def right_rotate(self, node) -> Node:
        l = node.left
        lr = l.right
        l.right = node
        node.left = lr
        lr.parent = node
        l.parent = node.parent
        node.parent = l

    # case: left right
    #         10 (node)
    #        /
    #       8
    #        \
    #         9
    # step: 1. left rotate 8, make it left left  2. right rotate
    def lr_rotate(self, node) -> Node:
        pass

    # case: right left
    #          10 (node)
    #           \
    #           15
    #          /
    #        12
    # step: 1. right rotate 15, make it right right  2. left rotate
    def rl_rotate(self, node) -> Node:
        pass
    
