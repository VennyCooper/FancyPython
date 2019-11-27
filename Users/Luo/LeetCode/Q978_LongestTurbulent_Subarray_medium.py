# A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:
#   For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
#   OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
# That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.
# Return the length of a maximum size turbulent subarray of A.

# Example 1:
#   Input: [9,4,2,10,7,8,8,1,9]
#   Output: 5
#   Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
# Example 2:
#   Input: [4,8,12,16]
#   Output: 2
# Example 3:
#   Input: [100]
#   Output: 1

# Note:
#   1 <= A.length <= 40000
#   0 <= A[i] <= 10^9

class Solution:
    def maxTurbulenceSize(self, A: list) -> int:
        A_len = len(A)
        if (A_len < 2):
            return A_len
        last_diff = 0
        max_len, tmp_len = 0, 0
        for i in range(A_len - 1):
            c = 1 if A[i + 1] > A[i] else (0 if A[i + 1] == A[i] else -1)
            if i == 0 or (i > 0 and c * last_diff != -1):
                tmp_len = 1 if c == 0 else 2
            else:
                tmp_len += 1
            last_diff = c
            max_len = max(max_len, tmp_len)
        return max_len


s = Solution()
A = [9,4,2,10,7,8,8,1,9]
B = [4,8,12,16]
C = [9,9]
print(s.maxTurbulenceSize(A))
print(s.maxTurbulenceSize(B))
print(s.maxTurbulenceSize(C))