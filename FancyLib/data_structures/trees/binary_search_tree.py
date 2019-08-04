from binary_tree import BinaryTree
from node import Node

class BinarySearchTree(BinaryTree):
    
    def is_tree_empty(self) -> bool:
        return self.root is None

    def is_node_left_child(self, node: Node) -> bool:
        return node == node.parent.left

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

    def get_node_level(self, data) -> int:
        node_found = self.search(data)
        if node_found is None:
            return -1
        level = 0
        tmp_node = node_found
        while tmp_node.parent is not None:
            tmp_node = tmp_node.parent
            level += 1
        return level
    
    '''
    Get node data of each level
    e.g.
        insert [50, 40, 60, 10, 80, 20, 70, 30, 9, 82] into the tree
                            50
                          /    \
                         40     60
                        /         \
                       10          80
                      /  \        /  \
                     9    20     70   82
                            \
                             30
        return [[50], [40, 60], [10, 80], [9, 20, 70, 82], [30]]
        (each index of the return list is the level)
    '''
    def get_nodes_at_each_level(self, root_node=None) -> list:
        if self.is_tree_empty():
            return []
        if root_node is None:
            root_node = self.root
        tree_depth = self.get_tree_depth()
        nodes = [[] for i in range(tree_depth)]
        tmp_queue = []
        tmp_queue.append(root_node)
        while len(tmp_queue) != 0:
            next_node = tmp_queue.pop(0)
            next_node_level = self.get_node_level(next_node.data)
            nodes[next_node_level].append(next_node.data)
            if next_node.left is not None:
                tmp_queue.append(next_node.left)
            if next_node.right is not None:
                tmp_queue.append(next_node.right)
        return nodes

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