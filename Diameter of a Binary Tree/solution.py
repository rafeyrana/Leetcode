# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        okay so this is not really a straightforward dfs because the dfs only returns the height
        so we need the height on both sides of each node and then compare it while we make our way back to the root
        in the recursive call, we need to keep a global variable to compare with the diameter
        but the dfs itself has to work as is because it is used to update the diameter at the node above as well


        using dfs to get height but keep a class variable using self.dia and in the dfs when getting left and right depths , just update the class variable to the max of class variable or left + right. return the class variable
        '''
        self.diameter = 0 # global variable linked to class

        def dfs(curr):
            if not curr:
                return 0

            # getting the height of the left and right sub trees
            left = dfs(curr.left)
            right = dfs(curr.right)        
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)
        dfs(root)
        return self.diameter