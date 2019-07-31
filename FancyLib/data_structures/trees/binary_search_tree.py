from tree import Tree
from node import Node

class BinarySearchTree(Tree):
    def delete(self, data):
        pass
    
    def is_tree_empty(self):
        return self.root is not None


    def search(self, data) -> Node:
        tmp_node = self.root
        while tmp_node != None:
            if data == tmp_node.data:
                break
            elif data < tmp_node.data:
                tmp_node = tmp_node.left
            else:
                tmp_node = tmp_node.right
        return tmp_node

