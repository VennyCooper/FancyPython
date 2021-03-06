# he Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Given two integers x and y, calculate the Hamming distance.

# Note:
# 0 ≤ x, y < 231.

# Example:
# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑

# The above arrows point to positions where the corresponding bits are different.

class Solution:
    def hammingDistance(self, x: int, y: int):
        xor = x ^ y
        dis = 0
        for i in str(bin(xor)):
            if i == '1':
                dis += 1
        return dis

    def hammingDistance_method2(self, x: int, y: int):
        dis = 0
        while x > 0 or y > 0:
            if x % 2 != y % 2:
                dis += 1
            x //= 2
            y //= 2
        return dis


s = Solution()
print(s.hammingDistance_method2(1, 4))