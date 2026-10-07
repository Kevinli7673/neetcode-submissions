class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l, r = 0, 0

        res = []


        while(l <= len(nums)-1 and r <= len(nums)-1):
            while nums[l] < 0:
                l += 1
            
            while nums[r] > 0:
                r += 1
            
            res.append(nums[l])
            res.append(nums[r])
            l += 1
            r += 1
        
        
        return res
