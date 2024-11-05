# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        using a recursive approach, if the node val is greater than the max on the path then increment the count
        keep a track of the max value on each path update it if you find a good node and increment the count
        start function with root and -inf
        '''
        self.good_node_count = 0
        def counter(node, max_on_path):
            if node:
                if node.val >= max_on_path:
                    max_on_path = node.val
                    self.good_node_count += 1
                counter(node.left, max_on_path)
                counter(node.right,max_on_path)


        counter(root, float("-inf"))
        return self.good_node_count
        
        
        