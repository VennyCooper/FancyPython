# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed.
# All houses at this place are arranged in a [[[[[circle]]]]].
# That means the first house is the neighbor of the last one.
# Meanwhile, adjacent houses have security system connected
# and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.

# Example 1:

# Input: [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
#              because they are adjacent houses.
# Example 2:

# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.


def rob(nums: list) -> int:
    nums_len = len(nums)
    if nums_len == 0:
        return 0
    if nums_len == 1:
        return nums[0]
    if nums_len == 2:
        return max(nums[:2])
    rob_include_1st = rob_in_range(nums[0:nums_len-1])
    rob_exclude_1st = rob_in_range(nums[1:nums_len])
    return max(rob_include_1st, rob_exclude_1st)


def rob_in_range(sub_nums: list) -> int:
    nums_len = len(sub_nums)
    d = [0 for n in range(nums_len)]
    d[0] = sub_nums[0]
    d[1] = max(sub_nums[:2])
    for i in range(2, nums_len):
        d[i] = max(sub_nums[i] + d[i - 2], d[i - 1])
    return d[nums_len - 1]



print(rob([1,2,3,1]))