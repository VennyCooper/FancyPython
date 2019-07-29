# Given a string, find the length of the longest substring without repeating characters.
# Example 1:
#   Input: "abcabcbb"
#   Output: 3 
#   Explanation: The answer is "abc", with the length of 3. 
# Example 2:
#   Input: "bbbbb"
#   Output: 1
#   Explanation: The answer is "b", with the length of 1.
# Example 3:
#   Input: "pwwkew"
#   Output: 3
#   Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Brute force O(n^3)
class Solution_1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_len = len(s)
        if s_len <= 1:
            return s_len
        sub_strs = []
        for i in range(s_len - 1):
            tmp = s[i]
            for j in range(i + 1, s_len):
                if s[j] not in tmp:
                    tmp += s[j]
                else:
                    break
            sub_strs.append(tmp)
        sub_strs = sorted(sub_strs, key=lambda x: len(x), reverse=True)
        return len(sub_strs[0])
    

# Sliding windos
class Solution_2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_len = len(s)
        if s_len <= 1:
            return s_len
        # store the last occurance index of each char
        char_dict = {}
        start_from = 0
        result_max = 0
        for i in range(s_len):
            if s[i] in char_dict:
                start_from = max(char_dict[s[i]] + 1, start_from)
            result_max = max(i - start_from + 1, result_max)
            char_dict[s[i]] = i
        return result_max



s = Solution_2()
print(s.lengthOfLongestSubstring("pwwkew"))