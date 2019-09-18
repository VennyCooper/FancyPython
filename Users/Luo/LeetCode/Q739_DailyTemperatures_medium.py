# Given a list of daily temperatures T, return a list such that, for each day in the input,
# tells you how many days you would have to wait until a warmer temperature.
# If there is no future day for which this is possible, put 0 instead.

# For example:
#   Given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73]
#   output should be [1, 1, 4, 2, 1, 1, 0, 0].

# Note:
#   The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].


class Solution:
    def dailyTemperatures(self, T):
        T_len = len(T)
        stack, days = [], [0] * T_len
        # reversely iterate the temperature list
        for i in range(T_len - 1, -1, -1):
            while stack:
                if T[stack[-1]] <= T[i]:
                    stack.pop()
                else:
                    break
            if stack:
                days[i] = stack[-1] - i
            stack.append(i)
        return days



s = Solution()

print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
