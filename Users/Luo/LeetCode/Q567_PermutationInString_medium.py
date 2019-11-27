# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
# In other words, one of the first string's permutations is the substring of the second string.

# Example 1:
#   Input: s1 = "ab" s2 = "eidbaooo"
#   Output: True
#   Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:
#   Input:s1= "ab" s2 = "eidboaoo"
#   Output: False

# Note:
#   The input strings only contain lower case letters.
#   The length of both given strings is in range [1, 10,000].

# Sliding window
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        if s1_len > s2_len:
            return False
        s1_arr = [0 for i in range(26)]
        s2_arr = [0 for i in range(26)]
        for i in range(s1_len):
            s1_arr[ord(s1[i]) - ord('a')] += 1
            s2_arr[ord(s2[i]) - ord('a')] += 1
        for i in range(s2_len - s1_len):
            if s1_arr == s2_arr:
                return True
            # move the slide window (s2 array) to the right
            s2_arr[ord(s2[i]) - ord('a')] -= 1
            s2_arr[ord(s2[i + s1_len]) - ord('a')] += 1
        return s1_arr == s2_arr


# Optimized sliding window
class Solution_2:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        if s1_len > s2_len:
            return False
        s1_arr = [0 for i in range(26)]
        s2_arr = [0 for i in range(26)]
        for i in range(s1_len):
            s1_arr[ord(s1[i]) - ord('a')] += 1
            s2_arr[ord(s2[i]) - ord('a')] += 1
        # if correct_count == 26 at the end, return true
        correct_count = sum(s1_arr[x] == s2_arr[x] for x in range(26))
        for i in range(s2_len - s1_len):
            if s1_arr == s2_arr:
                return True
            # move the slide window (s2 array) to the right
            s2_arr[ord(s2[i]) - ord('a')] -= 1
            s2_arr[ord(s2[i + s1_len]) - ord('a')] += 1
        return s1_arr == s2_arr



s1 = "ab"
s2 = "eidbaooo"
print(Solution_2().checkInclusion(s1, s2))
s1 = "ab"
s2 = "eidboaoo"
print(Solution_2().checkInclusion(s1, s2))