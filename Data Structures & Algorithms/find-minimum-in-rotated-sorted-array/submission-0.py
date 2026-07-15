"""
Brute force:
Iteartate through each array -> O(n)


"""

class Solution:
    def findMin(selef, nums: List[int]) -> int:
        res = nums[0]
        l,r = 0, len(nums)-1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(nums[l], res)
                break
            
            m = (l+r) // 2
            
            res = min(nums[m], res)
            if nums[m] >= nums[l]:
                l = m+1
            else:
                r = m-1
        return res