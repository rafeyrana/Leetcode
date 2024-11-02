# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        '''
        same thing as the same tree problem but run it on the current node, if not true then run a recursive call on the children nodes. this however is inefficient as it as it is O(n**2)
        there is a more optimal solution but that is too confusing and will not be asked in a real interview
        '''
        def same_tree(node, sub_tree):
            if not node and not sub_tree:
                return True
            if not node or not sub_tree:
                return False
            if node.val != sub_tree.val:
                return False
            return same_tree(node.left, sub_tree.left) and same_tree(node.right, sub_tree.right)

        if not root:
            return False
          
        # Check if the current tree matches subRoot or if subRoot is in either subtree of root
        return same_tree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
