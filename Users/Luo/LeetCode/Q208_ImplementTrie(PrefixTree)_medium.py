# Implement a trie with insert, search, and startsWith methods.

# Example:
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");
# trie.search("app");     // returns true

# Note:
#     You may assume that all inputs are consist of lowercase letters a-z.
#     All inputs are guaranteed to be non-empty strings.

# Structure
# class Trie:
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """

#     def insert(self, word: str) -> None:
#         """
#         Inserts a word into the trie.
#         """

#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the trie.
#         """

#     def startsWith(self, prefix: str) -> bool:
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         """

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tmp_node = self.root
        for c in word:
            if c not in tmp_node.children:
                tmp_node.children[c] = TrieNode()
            tmp_node = tmp_node.children[c]
        tmp_node.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tmp_node = self.root
        for c in word:
            if c not in tmp_node.children:
                return False
            tmp_node = tmp_node.children[c]
        return tmp_node.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tmp_node = self.root
        for c in prefix:
            if c not in tmp_node.children:
                return False
            tmp_node = tmp_node.children[c]
        return True


class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False



# Your Trie object will be instantiated and called as such:
trie = Trie()

trie.insert("apple");
apple_search0 = trie.search("apple");
app_search0 = trie.search("app");
app_pre = trie.startsWith("app");
trie.insert("app");
app_search = trie.search("app");
apple_search = trie.search("apple");
print()
