from tree import Tree
from node import Node

class BinarySearchTree(Tree):
    
    
    def is_tree_empty(self):
        return self.root is None


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
        pass
    
    def insert(self, data):
        if self.is_tree_empty():
            self.root = Node(data)
            return
        tmp_node = self.root
        while tmp_node is not None:
            if data > tmp_node.data:
                if tmp_node.right is None:
                    tmp_node.right = Node(data)
                    return
                tmp_node = tmp_node.right
            else:
                if tmp_node.left is None:
                    tmp_node.left = Node(data)
                    return
                tmp_node = tmp_node.left

bst = BinarySearchTree()
insert_nums = [50, 40, 60, 10, 80, 20, 70, 30]
for num in insert_nums:
    bst.insert(num)
bst.preorder_traversal(bst.root)
