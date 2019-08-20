from node import Node

class SinglyLinkedList:

    def __init__(self, head=None):
        self.head = None if head is None else head
    

    def is_empty(self) -> bool:
        return self.head is None


    def get_length(self, start_node=None) -> int:
        start_node = self.head if start_node is None else start_node
        length = 0
        start_node = self.head
        while start_node is not None:
            length += 1
            start_node = start_node.next_node
        return length


    def get_length_recursively(self, start_node: Node) -> int:
        if start_node is None:
            return 0
        else:
            return 1 + self.get_length_recursively(start_node.next_node)


    def print_linked_list(self):
        if self.head is None:
            print('HEAD: None (Linked list is empty )')
        else:
            print(f'HEAD: value = {self.head.data} | type = {type(self.head.data)}')
            msg = str(self.head.data)
            tmp_node = self.head.next_node
            while tmp_node is not None:
                msg += f' -> {str(tmp_node.data)}'
                tmp_node = tmp_node.next_node
            print(msg)


    def search(self, data) -> Node:
        tmp_node = self.head
        while tmp_node is not None:
            if tmp_node.data == data:
                return tmp_node
            tmp_node = tmp_node.next_node
        return None


    def append(self, data):
        self.insert_to_tail(data)


    def insert_to_tail(self, data):
        data_node = Node(data)
        if self.head is None:
            self.head = data_node
        else:
            tmp_node = self.head
            while tmp_node.next_node is not None:
                tmp_node = tmp_node.next_node
            tmp_node.next_node = data_node


    def push(self, data):
        self.insert_to_head(data)


    def insert_to_head(self, data):
        data_node = Node(data)
        data_node.next_node = self.head
        self.head = data_node

    
    def insert_after_node(self, data, prev_node: Node):
        if prev_node is None:
            return
        if self.search(prev_node.data) is None:
            return
        data_node = Node(data)
        data_node.next_node = prev_node.next_node
        prev_node.next_node = data_node


    # Delete the first occurrence of the given data node
    def delete_data(self, data):
        # return if linked list is empty (head is None)
        if self.is_empty():
            return
        prev_node = self.head
        if data == prev_node.data:
            self.head = prev_node.next_node
            prev_node = None
            return
        tmp_node = prev_node.next_node
        while tmp_node is not None:
            if data == tmp_node.data:
                prev_node.next_node = tmp_node.next_node
                tmp_node = None
                break
            prev_node = tmp_node
            tmp_node = tmp_node.next_node


    # Delete the first occurrence of the given node
    def delete_node(self, node: Node):
        self.delete_data(node.data)


    # Delete the node at the given index
    def delete_node_at_index(self, index: int):
        tmp_node = self.head
        if index == 0:
            self.head = tmp_node.next_node
            tmp_node = None
            return
        # find the previous node of the index-th node
        for i in range(index - 1):
            tmp_node = tmp_node.next_node
            if tmp_node is None:
                return
        # now tmp_node is the previous node of the index-th node
        if tmp_node.next_node is None:
            return 
        next = tmp_node.next_node.next_node
        tmp_node.next_node = None
        tmp_node.next_node = next


    # get the n-th node from the end (end is the 1st node)
    def get_nth_node_from_end(self, n: int) -> Node:
        length = self.get_length()
        if n > length:
            print(f'Error: The given n = {n} is larger than the length = {length} of the linked list')
            return
        tmp_node = self.head
        for i in range(length - n):
            tmp_node = tmp_node.next_node
        return tmp_node
        
    # get the n-th node from the end (end is the 1st node) using two-pointer method
    def get_nth_node_data_from_end_twoPointers(self, n: int) -> Node:
        # 1. Define two pointers, both point to the head node
        # 2. Move pointer 1 to the n-th node from head node
        # 3. Move both pointers one by one until pointer 1 reaches the end node
        # => Pointer 2 will point to the required node when pointer 1 stops
        pointer_1 = self.head
        pointer_2 = self.head
        for i in range(n):
            if pointer_1 is None:
                print(f'Error: The given n = {n} is larger than the length of the linked list')
            pointer_1 = pointer_1.next_node
        while pointer_1 is not None:
            pointer_1 = pointer_1.next_node
            pointer_2 = pointer_2.next_node
        return pointer_2


    def reverse(self):
        # None -> head -> 1 -> 2 -> ...
        tmp_node = self.head
        prev_node = None
        while tmp_node is not None:
            next_node = tmp_node.next_node
            tmp_node.next_node = prev_node
            prev_node = tmp_node
            tmp_node = next_node
        self.head = prev_node




s = SinglyLinkedList()
data = [90,100,3,1,24,8,66]
for d in data:
    s.insert_to_tail(d)
s.print_linked_list()
s.reverse()
s.print_linked_list()
