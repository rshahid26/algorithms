class TrieNode():
    def __init__(self):
        self.children = {}
        self.end_of_word = False
    
    def has(self, char):
        return char in self.children
    
    def is_empty(self):
        return len(self.children) == 0

class Trie():
    def __init__(self, words: list = None):
        self.root = TrieNode()
        for word in words:
            self.insert(word)
    
    def insert(self, word):
        node = self.root
        for char in word:
            if not node.has(char):
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if not node.has(char):
                return False
            node = node.children[char]
        return node.end_of_word
    
    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if not node.has(char):
                return False
            node = node.children[char]
        return True
    
    def delete(self, word):
        def _delete(node, i):
            if i == len(word):
                return node.is_empty() and node.end_of_word
            if not node.has(word[i]):
                return False
            
            if _delete(node.children[word[i]], i + 1):
                del node.children[word[i]]
                return node.is_empty()
            return False

        _delete(self.root, 0)
