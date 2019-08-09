from node import Node 
class BinaryTree:

    def __init__(self, data=None):
        self.root = None if data == None else Node(data)
    

    def is_tree_empty(self) -> bool:
        return self.root is None


    def is_node_left_child(self, node: Node) -> bool:
        return node == node.parent.left


    def insert(self, data):
        pass
    

    def delete(self, data):
        pass
    

    def search(self, data) -> Node:
        pass
    

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


    def get_tree_depth(self) -> int:
        return self.get_depth_from_node(self.root)


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


    def get_depth_from_node(self, start_node: Node) -> int:
        if start_node is None:
            return 0
        left_child_depth = self.get_depth_from_node(start_node.left)
        right_child_depth = self.get_depth_from_node(start_node.right)
        return max(left_child_depth + 1, right_child_depth + 1)


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


    def print_tree(self):
        nodes_at_levels = self.get_nodes_at_each_level()
        max_items_at_level = max((len(i) for i in nodes_at_levels))
        pass

