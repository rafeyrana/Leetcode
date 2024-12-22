class TreeNode:
    def __init__(self):
        self.children = {}  # Mapping from characters to child nodes
        self.isWord = False  # Flag indicating if this node represents the end of a word

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()  # Root of the trie

    def addWord(self, word: str) -> None:
        curr_node = self.root
        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = TreeNode()
            curr_node = curr_node.children[c]
        curr_node.isWord = True  # Mark the end of the word

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):  # Base case: If we've processed the entire word
                return node.isWord
            c = word[index]
            if c == '.':  # Wildcard character
                # Check all possible child nodes
                return any(dfs(child, index + 1) for child in node.children.values())
            if c not in node.children:  # Character not found
                return False
            # Proceed to the next character
            return dfs(node.children[c], index + 1)
        
        return dfs(self.root, 0)
