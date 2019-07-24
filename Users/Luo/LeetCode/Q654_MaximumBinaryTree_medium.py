# Given an integer array with no duplicates. A maximum tree building on this array is defined as follow: 
#   The root is the maximum number in the array. 
#   The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
#   The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.

# Construct the maximum tree by the given array and output the root node of this tree. 

# Example 1:
#   Input: [3,2,1,6,0,5]
#   Output: return the tree root node representing the following tree:

#       6
#     /   \
#    3     5
#     \    / 
#      2  0   
#        \
#         1

# Note:
#   The size of the given array will be in the range [1,1000].

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums) -> TreeNode:
        a = self.construct_max_bin_tree(nums, 0, len(nums))
        return a
    
    def construct_max_bin_tree(self, nums, start: int, stop: int) -> TreeNode:
        if start >= stop:
            return None
        max_index = self.get_max_num_index_in_range(nums, start, stop)
        root = TreeNode(nums[max_index])
        root.left = self.construct_max_bin_tree(nums, 0, max_index)
        root.right = self.construct_max_bin_tree(nums, max_index + 1, stop)
        return root
    
    def get_max_num_index_in_range(self, nums, start: int, stop: int) -> int:
        max_index = start
        for i in range(start, stop):
            if nums[i] > nums[max_index]:
                max_index = i
        return max_index

s = Solution()
b = s.constructMaximumBinaryTree([3,2,1,6,0,5])