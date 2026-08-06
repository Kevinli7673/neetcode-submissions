"""
DFS: Move down the tree until you reach a dead end, then back up to the last unexplored branch and go down again. Achieve this either by recursion (each call handles a child, backing up happens on return) or by an explicit stack (push children, pop to go deeper — LIFO). Using a queue instead would make it BFS.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None

        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left   # <-- the flip, done here
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root