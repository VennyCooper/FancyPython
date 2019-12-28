# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

# Example 1:
# Input: [3,0,1]
# Output: 2

# Example 2:
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8

# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

class Solution:
    def missingNumber(self, nums: list) -> int:
        result = len(nums)
        for i in range(result):
            result ^= i ^ nums[i]
        return result

    def missingNumber_GaussSum(self, nums: list) -> int:
        n_len = len(nums)
        expected_sum = n_len * (n_len + 1) // 2
        actual_sum = 0
        for n in nums:
            actual_sum += n
        return expected_sum - actual_sum

s = Solution()
print(s.missingNumber_GaussSum([0,1,3]))