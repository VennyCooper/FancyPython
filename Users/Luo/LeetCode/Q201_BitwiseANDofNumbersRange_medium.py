# Given a range [m, n] where 0 <= m <= n <= 2147483647,
# return the bitwise AND of all numbers in this range, inclusive.

# Example 1:
#   Input: [5,7]
#   Output: 4

# Example 2:
#   Input: [0,1]
#   Output: 0

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == n:
            return m
        if m <= 1:
            return 0
        diff_bits_count = 0
        while m != n:
            m >>= 1
            n >>= 1
            diff_bits_count += 1
        return m << diff_bits_count

    def rangeBitwiseAnd_2(self, m: int, n: int) -> int:
        if m == n:
            return m
        if m <= 1:
            return 0
        while m < n:
            n &= n - 1
        return n

s = Solution()
print(s.rangeBitwiseAnd_2(5,7))
print(s.rangeBitwiseAnd_2(0,1))