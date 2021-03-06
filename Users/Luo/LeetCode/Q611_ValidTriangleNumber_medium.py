# Given an array consists of non-negative integers,
# your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

# Example 1:

# Input: [2,2,3,4]
# Output: 3
# Explanation:
#   Valid combinations are:
#   2,3,4 (using the first 2)
#   2,3,4 (using the second 2)
#   2,2,3

# Note:
#     The length of the given array won't exceed 1000.
#     The integers in the given array are in the range of [0, 1000].


class Solution:
    def triangleNumber(self, nums: list) -> int:
        result = 0
        n_len = len(nums)
        if n_len < 3:
            return result
        nums = sorted(nums)
        for k in range(2, n_len):
            l, r = 0, k - 1
            if nums[r] + nums[r-1] <= nums[k]:
                continue
            while l < r:
                if nums[l] + nums[r] > nums[k]:
                    result += r - l
                    r -= 1
                else:
                    l += 1
        return result



s = Solution()
print(s.triangleNumber([2,2,3,4]))