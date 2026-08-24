# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Idea: for dfs we do root.right and root.left and when we find a 
option option we add to the stack
when we hit null on both left and right we calculate the diameter
and reset back to the subroot
"""
"""
stack []
curr: 2
height: 1
dummy: 2
res = 2
"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res
            if not root:
                return 0

            curr_right = dfs(root.right)
            curr_left = dfs(root.left)
            res = max(res, curr_right + curr_left)
            return max(curr_right, curr_left) + 1

        dfs(root)
        return res
            
            
            