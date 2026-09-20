# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        val = 0
        res = 0

        def dfs(node):
            nonlocal val
            nonlocal res

            if res: 
                return res
            if not node:
                return

            dfs(node.left)
            val += 1
            print(node.val, val)
            if(val == k):
                res = node.val

            dfs(node.right)

        dfs(root)
        return res