# Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive linked list "parts". 
# The length of each part should be as equal as possible: no two parts should have a size differing by more than 1. 
# This may lead to some parts being null. 
# The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later. 
# Return a List of ListNode's representing the linked list parts that are formed. 

# Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ] 

# Example 1:
# Input: 
#   root = [1, 2, 3], k = 5
#   Output: [[1],[2],[3],[],[]]
# Explanation:
#   The input and each element of the output are ListNodes, not arrays.
#   For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3, and root.next.next.next = null.
#   The first element output[0] has output[0].val = 1, output[0].next = null.
#   The last element output[4] is null, but it's string representation as a ListNode is [].

# Example 2:
# Input: 
#   root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
#   Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
# Explanation:
#   The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.

# Note: 
#   The length of root will be in the range [0, 1000].
#   Each value of a node in the input will be an integer in the range [0, 999].
#   k will be an integer in the range [1, 50].


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int):
        result = []
        tmp = root
        # calculate length of linked list
        length = 0
        while tmp is not None:
            length += 1
            tmp = tmp.next
        # re-point tmp to the head (root) of linked list
        tmp = root
        div_size = length // k
        remainder = length % k
        for i in range(k):
            actual_div_size = div_size + 1 if i < remainder else div_size
            element = None
            element_tmp = None
            for j in range(actual_div_size):
                if j == 0:
                    element = ListNode(tmp.val)
                    element_tmp = element
                else:
                    element_tmp.next = ListNode(tmp.val)
                    element_tmp = element_tmp.next
                tmp = tmp.next
            result.append(element)
        return result



def print_list(head:ListNode):
    t_node = head
    result = ''
    while t_node is not None:
        result += str(t_node.val) + ' -> '
        t_node = t_node.next
    result += 'None'
    print(result)

root = [1, 2, 3, 4, 5, 6, 7]
k = 3
head = ListNode(root[0])
t_node = head
for i in root[1:]:
    t_node.next = ListNode(i)
    t_node = t_node.next
s = Solution()
for x in s.splitListToParts(head, k):
    print_list(x)
