# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""

"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, minval, maxval):

            if not node:
                return True
            
            if node.val > maxval or node.val < minval:
                return False

            return dfs(node.right, node.val+1, maxval) and dfs(node.left, minval, node.val-1)

        
        return dfs(root, float('-inf'), float('inf'))