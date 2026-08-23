# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 0)]
        res = 0

        while stack:
            curr, height = stack.pop()
            if curr == None:
                continue
            if curr.left:
                stack.append((curr.left, height+1))
            if curr.right:
                stack.append((curr.right, height+1))
            res = max(res, height+1)

        return res