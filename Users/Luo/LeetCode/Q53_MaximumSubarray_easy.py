# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:
#   Input: [-2,1,-3,4,-1,2,1,-5,4],
#   Output: 6
#   Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
#   If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

class Solution_1:
    def maxSubArray(self, nums) -> int:
        nums_len = len(nums)
        if nums_len == 0:
            raise Exception('Error: nums cannot be empty.')
        cur_sum = nums[0]
        result_sum = sum(nums)
        for i in range(nums_len):
            cur_sum += nums[i]
            if cur_sum > result_sum:
                result_sum = cur_sum
            if cur_sum < 0:
                cur_sum = 0
        return result_sum


class Solution_2:
    def maxSubArray(self, nums) -> int:
        pass