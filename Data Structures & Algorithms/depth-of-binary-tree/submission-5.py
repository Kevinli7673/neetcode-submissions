# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append((root, 0))
        res = 0
        

        while queue:
            curr, height = queue.pop()
            if not curr:
                continue
            queue.appendleft((curr.right, height+1))
            queue.appendleft((curr.left, height+1))
            res = max(res, height + 1)

        return res