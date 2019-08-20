class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node if next_node is not None else next_node
