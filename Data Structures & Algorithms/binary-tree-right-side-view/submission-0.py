# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
We can incorporate height + set: We use dfs(node, height) and we if the height
exist in the set yet, if not, its the most right and we add it to set
"""

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        seen = set()
        height = 0

        def dfs(node, height):
            if not node:
                return 

            if height not in seen:
                res.append(node.val)
                seen.add(height)

            dfs(node.right, height+1)
            dfs(node.left, height+1)
        
        dfs(root, 0)
        return res