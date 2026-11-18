"""
Idea: we have pointer left and right ends of the array
We iterate the pointer that is smaller, while keeping max
this way we can find maxiumum chance

[1, 7, 6, 7, 500, 500, 20, 1, 4, 8]
"""
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        most = 0
            
        while(l < r):
            curr = (r - l) * min(heights[l], heights[r])
            if curr > most:
                most = curr
            if(heights[l] <= heights[r]):
                l += 1
            elif(heights[r] <= heights[l]):
                r -= 1
        
        return most