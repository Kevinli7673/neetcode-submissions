# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Dfs: Since this is a binary search tree we can search for the first value that is bigger than or equal to p and smaller than or equal to q
"""

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        res = None
        
        def dfs(tree):
            nonlocal res

            if not tree or res:
                return
            
            if p.val < q.val:
                if tree.val >= p.val and tree.val <= q.val:
                    res = tree
            elif p.val > q.val:
                if tree.val <= p.val and tree.val >= q.val:
                    res = tree

            dfs(tree.right)
            dfs(tree.left)

        dfs(root)

        return res