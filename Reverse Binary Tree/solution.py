# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# using a recursive approach, if at root does not exist return None, swap the root.left and root.right (can be done in place or using a temp variable) and recurse on the left and right subtrees, return root


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        temp = root.left
        root.left = root.right
        root.right = temp
        # root.left , root.right = root.right, root.left # this is the inline approach in python
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root