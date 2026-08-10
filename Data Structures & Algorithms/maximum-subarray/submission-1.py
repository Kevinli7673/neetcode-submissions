"""
Find a subarray that has the biggest sum
Idea: We grab the first val: 
      If its negative, we pop and keep moving until we we're positive (if len > 1)
      If we're positive, calculate the max, then we continue, if the next value
      makes out res negative, we pop both and continue
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, curSum = nums[0], 0
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSub = max(maxSub, curSum)
        return maxSub