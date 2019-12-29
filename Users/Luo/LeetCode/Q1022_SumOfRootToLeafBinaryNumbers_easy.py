# Given a binary tree, each node has value 0 or 1.
# Each root-to-leaf path represents a binary number starting with the most significant bit.
# For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.
# Return the sum of these numbers.

# Example 1:
#   Input: [1,0,1,0,1,0,1]
#        1
#     0      1
#   0   1   0  1
#   Output: 22
#   Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

# Note:
#     The number of nodes in the tree is between 1 and 1000.
#     node.val is 0 or 1.
#     The answer will not exceed 2^31 - 1.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.result = 0
        def traverse_recursive(root, path):
            if root.left:
                traverse_recursive(root.left, path + str(root.val))
            if root.right:
                traverse_recursive(root.right, path + str(root.val))
            if not root.left and not root.right:
                self.result += int(path + str(root.val), 2)
        traverse_recursive(root, '')
        return self.result

    def sumRootToLeaf_stack(self, root: TreeNode) -> int:
        result = 0
        stack = [[root, '']]
        while stack:
            node = stack.pop(0)
            node_val = node[1] + str(node[0].val)
            if node[0].left:
                stack.append([node[0].left, node_val])
            if node[0].right:
                stack.append([node[0].right, node_val])
            if not node[0].left and not node[0].right:
                result += int(node_val, 2)
        return result
