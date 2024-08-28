# delete a node in trie -> boarding week questions
# graph implementation -> dfs
# delete root node in bst if root node has 2 children otherwise not

# The basic functions of a trie include: insert, 
# search a word, and search a prefix implemented using
# dictionary or hash table here not using linked list:
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
 
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def start_with(self,prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# implement trie using Linked List