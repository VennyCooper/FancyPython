from binary_tree import BinaryTree
from node import Node

'''
    Methods that keep same as in base class BinaryTree:
        1. is_tree_empty(self) -> bool
        2. is_node_left_child(self, node: Node) -> bool
        3. preorder_traversal(self, root_node: Node)
        4. postorder_traversal(self, root_node: Node)
        5. inorder_traversal(self, root_node: Node)
        6. get_tree_depth(self) -> int
        7. get_node_level(self, data) -> int
        8. get_depth_from_node(self, start_node: Node) -> int
        9. get_nodes_at_each_level(self, root_node=None) -> list
        10. print_tree(self)
'''

class BinarySearchTree(BinaryTree):
    
    def replace_node(self, old_node: Node, new_node: Node):
        if new_node is not None:
            new_node.parent = old_node.parent
        if old_node.parent is not None:
            if self.is_node_left_child(old_node):
                old_node.parent.left = new_node
            else:
                old_node.parent.right = new_node


    def get_node_with_max_data(self, root_node=None) -> Node:
        tmp_node = self.root if root_node is None else root_node
        while tmp_node.right is not None:
            tmp_node = tmp_node.right
        return tmp_node


    def get_node_with_min_data(self, root_node=None) -> Node:
        tmp_node = self.root if root_node is None else root_node
        while tmp_node.left is not None:
            tmp_node = tmp_node.left
        return tmp_node


    def search(self, data) -> Node:
        tmp_node = self.root
        while tmp_node is not None:
            if data == tmp_node.data:
                break
            elif data < tmp_node.data:
                tmp_node = tmp_node.left
            else:
                tmp_node = tmp_node.right
        return tmp_node
    

    def delete(self, data):
        # if empty tree
        if self.is_tree_empty():
            return
        data_node = self.search(data)
        # if there is no node with this data
        if data_node is None:
            return
        # to delete the leaf node
        if data_node.left is None and data_node.right is None:
            self.replace_node(data_node, None)
        # to delete a node that only has the right child
        elif data_node.left is None and data_node.right is not None:
            self.replace_node(data_node, data_node.right)
        # to delete a node that only has the left child
        elif data_node.left is not None and data_node.right is None:
            self.replace_node(data_node, data_node.left)
        # to delete a node that have both left and right children:
        else:
            # find the node with the minimum data (M) in the right child
            # delete M from the right child
            # replace the data_node with M
            # because: maximum of left child < M < others in the right child
            right_child_min_node = self.get_node_with_min_data(data_node.right)
            self.delete(right_child_min_node.data)
            data_node.data = right_child_min_node.data


    def insert(self, data):
        node_to_insert = Node(data)
        if self.is_tree_empty():
            self.root = node_to_insert
            return
        tmp_node = self.root
        while tmp_node is not None:
            if data > tmp_node.data:
                if tmp_node.right is None:
                    tmp_node.right = node_to_insert
                    break
                tmp_node = tmp_node.right
            else:
                if tmp_node.left is None:
                    tmp_node.left = node_to_insert
                    break
                tmp_node = tmp_node.left
        node_to_insert.parent = tmp_node



test = True
if test:
    bst = BinarySearchTree()
    insert_nums = [50, 40, 60, 10, 80, 20, 70, 30, 9, 82]
    for num in insert_nums:
        bst.insert(num)
    bst.preorder_traversal(bst.root)
    # bst.delete(50)
    # print('====================')
    # bst.preorder_traversal(bst.root)
    # print(bst.get_nodes_at_each_level())
    print(bst.get_nodes_at_each_level())