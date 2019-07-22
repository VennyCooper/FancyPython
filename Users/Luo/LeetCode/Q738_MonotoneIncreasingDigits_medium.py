# Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits. 
# (Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.) 

# Example 1:
# Input: N = 10
# Output: 9

# Example 2:
# Input: N = 1234
# Output: 1234

# Example 3:
# Input: N = 332
# Output: 299

# Note: N is an integer in the range [0, 10^9]. 

class Solution:
    def monotoneIncreasingDigits(self, N: int):
        N_str = str(N)
        digit_count = len(N_str)
        result_str = ''
        for i in range(digit_count - 1, 0, -1):
            if N_str[i] < N_str[i - 1]:
                N_str[i] = '9'
                N_str[i - 1] = 

s = Solution()
s.monotoneIncreasingDigits(345)