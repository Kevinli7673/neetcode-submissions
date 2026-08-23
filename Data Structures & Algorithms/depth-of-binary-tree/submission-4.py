# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res, height = 0, 0

        def dfs(head, height):
            nonlocal res
            if not head:
                return 
            res = max(res, height+1)
            dfs(head.right, height+1)
            dfs(head.left, height+1)


        dfs(root, 0)
        return res