from data_structures.Trie import Trie

trie = Trie()
trie.insert("apple")
trie.search("apple") # True
trie.search("app") # False
trie.startsWith("app") # True
trie.insert("app")
trie.search("app") # True
trie.delete("appl") # Does nothing, word doesn't exist
trie.delete("apple")
trie.search("apple") # False
trie.search("app") # True

trie2 = Trie(["cat", "cater", "cats"])
trie.delete("cats")
trie.search("cat") # True