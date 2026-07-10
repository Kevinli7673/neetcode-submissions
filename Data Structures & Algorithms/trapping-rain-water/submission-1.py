"""
Water is traped between two elevation that is higher than 0
If not, water isn't trapped
"""
"""
height = [0,2,0,3,1,0,1,3,2,1]

l = 0 r = 2
water = 0 duds = 0
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        
        l,r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while(l < r):
            if leftMax <= rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res