# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
We're checking if the subroot exist in our main tree, we can the previous function that compare the two trees. So everytime our curr node is teh same value of subroot we run the checksame function
"""

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = False

        def checkTree(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False

            right = checkTree(l.right, r.right)
            left = checkTree(l.left, r.left)

            return l.val == r.val and right and left
        
        def dfs(node):
            nonlocal res
            if not node:
                return

            dfs(node.right)
            dfs(node.left)

            if (node.val == subRoot.val):
                check = checkTree(node, subRoot)
                if check == True:
                    res = check

        dfs(root)
        return res