"""
Brute force:
loop through each element (but not O(logn))
idea:
Use three pointers, one at front, middle, and end
Check if the middle pointer is bigger or smaller, and make that one of the end
Do that until target is found

nums = [-1,0,2,4,6,8], target = 4
             
l = 0     
r = 5
m = 2
""" 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while(l <= r):
            m = l+((r-l)//2)
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
                
        return -1