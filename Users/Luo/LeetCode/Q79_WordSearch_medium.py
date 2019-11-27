# Given a 2D board and a word, find if the word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
# Example:
    # board =
    # [
    #   ['A','B','C','E'],
    #   ['S','F','C','S'],
    #   ['A','D','E','E']
    # ]

# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.

class Solution:
    def exist(self, board, word: str) -> bool:
        if len(word) == 0:
            return True
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.find_word(board, word, i, j, 0):
                    return True
        return False

    def find_word(self, board, word, i, j, w_index) -> bool:
        if w_index == len(word):
            return True
        if i < 0 or j < 0:
            return False
        if i == len(board) or j == len(board[i]):
            return False
        if board[i][j] == '.':
            return False
        if board[i][j] != word[w_index]:
            return False
        tmp = board[i][j]
        board[i][j] = '.'
        has_found = self.find_word(board, word, i + 1, j, w_index + 1) or self.find_word(board, word, i - 1, j, w_index + 1) \
            or self.find_word(board, word, i, j + 1, w_index + 1) or self.find_word(board, word, i, j - 1, w_index + 1)
        board[i][j] = tmp
        return has_found


s = Solution()
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

print(s.exist(board, "ABCCED"))
print(s.exist(board, "SEE"))
print(s.exist(board, "ABCB"))