"""
We can use DFS: we continue one side until we reach the end
Whenever there is another option: we add that to the queue

Edge case: Check if root exist
Things to watch out: 
Keep track of the counter is easy in the beginning, but how do we 
move back in the tree and find the layer?
Idea: Use a tuple (root, counter)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        maxdepth, depth = 1, 1
        queue = [(root, depth)]

        """
        queue = [(2,2))(4,3)]
        curr = 3
        depth = 3
        maxdepth(3)
        """
        while queue:
            curr, depth = queue.pop()
            
            
            if curr.left:
                queue.append((curr.left, depth+1))
            if curr.right:
                queue.append((curr.right, depth+1))

            maxdepth = max(maxdepth, depth)

        return maxdepth