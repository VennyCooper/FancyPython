# Given an array A of non-negative integers, return an array consisting of all the even elements of A,
# followed by all the odd elements of A.
# You may return any answer array that satisfies this condition.

# Example 1:
#   Input: [3,1,2,4]
#   Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

class Solution:
    def sortArrayByParity(self, A: list) -> list:
        A_len = len(A)
        l, r = 0, A_len - 1
        while l != r:
            if A[l] % 2 != 0:
                if A[r] % 2 == 0:
                    A[l] ^= A[r]
                    A[r] ^= A[l]
                    A[l] ^= A[r]
                else:
                    r -= 1
            else:
                l += 1
        return A

s = Solution()
print(s.sortArrayByParity([3,1,2,4]))