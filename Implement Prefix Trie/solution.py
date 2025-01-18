class TreeNode:
    def __init__(self):
        self.chars = {} # this will contain the mapping from the characters to the their nodes in the tree and if they are a word or not (char : (Node, isWord))

    def insertChar(self,c):
        self.chars[c] = [TreeNode(), False]

class PrefixTree:
    def __init__(self):
        self.root = TreeNode() # the main root which will be the origin for each word search from origin
        
    def insert(self, word: str) -> None:
        curr_node = self.root
        for i in range(len(word)):
            c = word[i]
            if c not in curr_node.chars:
                # if this character is not in the current nodes mappings we will create it for them using the insertChar one
                curr_node.insertChar(c)
            if i == len(word) - 1:
                curr_node.chars[c][1] = True
            curr_node = curr_node.chars[c][0]

    def search(self, word: str) -> bool:
        curr_node = self.root 
        for i in range(len(word)):
            c = word[i]
            if c not in curr_node.chars:
                return False
            if i == len(word) - 1:
                if not curr_node.chars[c][1]:
                    return False
            curr_node = curr_node.chars[c][0]
        return True
            
    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root 
        for i in range(len(prefix)):
            c = prefix[i]
            if c not in curr_node.chars:
                return False
            curr_node = curr_node.chars[c][0]
        return True
    