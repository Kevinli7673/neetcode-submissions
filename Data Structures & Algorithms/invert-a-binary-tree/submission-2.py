# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        dummy = root
        queue = deque()

        def bfs(root):
            queue.append(dummy)
            while queue:
                root = queue.pop()
                if root == None:
                    continue
                root.left, root.right = root.right, root.left
                queue.appendleft(root.left)
                queue.appendleft(root.right)

            

        
        bfs(dummy)
        return root