"""
Pretty much, return the number in ascending order
Ideas: frequency map (only issue, doesn't cover follow up)

How do we come up with a one-pass alg with constant extra space?
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        freq = {0:0,1:0,2:0}
        res = []

        for num in nums:
            freq[num] += 1
        
        for key in freq:
            for i in range(freq[key]):
                res.append(key)
                print(res)

        nums[:] = res
