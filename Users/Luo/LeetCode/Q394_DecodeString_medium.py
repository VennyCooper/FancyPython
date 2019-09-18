# Given an encoded string, return its decoded string.
# The encoding rule is:
#   k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.
#   (Note that k is guaranteed to be a positive integer.)
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k.
# For example, there won't be input like 3a or 2[4].
# Examples:
#   s = "3[a]2[bc]", return "aaabcbc".
#   s = "3[a2[c]]", return "accaccacc".
#   s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        # stack[0][0] is the result
        stack.append(['', 1])
        tmp_s, k = '', ''
        for c in s:
            # Cond.1: c is the digit of k
            if c.isdigit():
                k += c
            # Cond.2: c is left bracket
            elif c == '[':
                # push current bracket to stack top
                stack.append(['', k])
                k = ''
            # Cond.3: c is right bracket
            elif c == ']':
                [tmp_s, k] = stack.pop()
                # add tmp string to its parent string
                stack[-1][0] += tmp_s * int(k)
                tmp_s, k = '', ''
            # Cond.4: c is the char inside the bracket
            else:
                # (stack top) string joint
                stack[-1][0] += c
        return stack[0][0] * stack[0][1]

s = Solution()
ss = '3[a2[c]]'
print(s.decodeString(ss))