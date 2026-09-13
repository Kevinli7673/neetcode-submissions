# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
dfs(node, biggestval) - if our curr val >= biggestval, its good
else, we replace biggest val with curr val

"""
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 0

        def dfs(node, biggestVal):
            nonlocal res
            if not node:
                return

            if node.val >= biggestVal:
                res += 1
                biggestVal = node.val

            dfs(node.right, biggestVal)
            dfs(node.left, biggestVal)

        dfs(root, root.val)
        return res