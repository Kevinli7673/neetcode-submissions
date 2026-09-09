# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        temp = []
        queue = deque()
        prevcount = 0

        if not root:
            return res
        
        queue.append((root, prevcount))

        while queue:
            curr, level = queue.pop()

            if level != prevcount:
                res.append(temp)
                temp = []
                prevcount = level
            
            if curr.left:
                queue.appendleft((curr.left, level+1))
            if curr.right:
                queue.appendleft((curr.right, level+1))
            
            temp.append(curr.val)
        
        if temp:
            res.append(temp)
        
        return res