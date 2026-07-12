"""
Create a emty array the length of nums * 2
For each element in nums, add it to its index and index + len(nums) - 1
"""

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = [0] * (len(nums) * 2)

        for i in range(len(nums)):
            res[i] = nums[i]
            res[i + len(nums)] = nums[i]

        return res
