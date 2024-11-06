# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    '''
    store the nodes and nulls using dfs in a string. perform preorder traversal to get the string. for deserialize keep a pointer which points to the current node. make a new dfs function that will return None if val is "N" else make a new node and call the function on the left and right of that new node. increment the global pointer pointing to the current node in the serialized string. in the end just return the root from the first call of the function'''
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.serial = []
        def dfs(node):
            if not node:
                self.serial.append("N")
                return
            self.serial.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(self.serial)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.current_node = 0

        def dfs():
            if vals[self.current_node] == "N":
                self.current_node += 1
                return None
            
            node = TreeNode(int(vals[self.current_node]))
            self.current_node += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()



