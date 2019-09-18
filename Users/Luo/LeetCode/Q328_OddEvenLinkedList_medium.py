# Given a singly linked list, group all odd nodes together followed by the even nodes. 
# Please note here we are talking about the node number and not the value in the nodes.
# You should try to do it in place. 
# The program should run in O(1) space complexity and O(nodes) time complexity.

# Example 1:
#    Input: 1->2->3->4->5->NULL
#    Output: 1->3->5->2->4->NULL

# Example 2:
#    Input: 2->1->3->5->6->4->7->NULL
#    Output: 2->3->6->7->1->5->4->NULL

# Note:
#    The relative order inside both the even and odd groups should remain as it was in the input.
#    The first node is considered odd, the second node even and so on ...

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        o = head
        e = head.next
        if e is None:
            return head
        e_head = e
        while e.next is not None:
            o.next = e.next
            o = e.next
            if o.next is None:
                e.next = None
                break
            e.next = o.next
            e = o.next
        o.next = e_head
        
        return head
            


def print_list(head:ListNode):
    t_node = head
    result = ''
    while t_node is not None:
        result += str(t_node.val) + ' -> '
        t_node = t_node.next
    result += 'None'
    print(result)

head = ListNode(1)
t_node = head
for i in [2,3,4,5,6,7]:
    t_node.next = ListNode(i)
    t_node = t_node.next

# print_list(head)
s = Solution()
print_list(s.oddEvenList(head))

