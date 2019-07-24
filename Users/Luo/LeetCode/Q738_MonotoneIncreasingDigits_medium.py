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
        N_list = list(str(N))
        cliff_end = 0
        N_len = len(N_list)
        while cliff_end < N_len - 1 and N_list[cliff_end] <= N_list[cliff_end + 1]:
            cliff_end += 1
        start = cliff_end + 1
        while 0 < start < N_len and N_list[start - 1] > N_list[start]:
            start -= 1
            N_list[start] = str(int(N_list[start]) - 1)
        N_list[start + 1:] = '9' * (N_len - start - 1)
        return int(''.join(N_list))

s = Solution()
print(s.monotoneIncreasingDigits(12231))