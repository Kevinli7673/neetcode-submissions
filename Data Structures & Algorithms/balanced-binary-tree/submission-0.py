# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Idea: We can search the tree 2 times, left and right
Then we do DFS starting on the left and right node
Then for each time we do .right or .next, we have to add that to stack
we're gonna have to keep adding 
"""
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True

        left = root.left
        right = root.right
        l = r = 0
        def DFS(node):
            if not node:
                return 0
            return 1 + max(DFS(node.left), DFS(node.right))
        
        balanced_here = abs(DFS(root.left) - DFS(root.right)) <= 1
        return balanced_here and self.isBalanced(root.left) and        self.isBalanced(root.right)

