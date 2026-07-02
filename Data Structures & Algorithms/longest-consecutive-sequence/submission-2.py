class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = tuple(set(nums))
        maximum, i= 0, 0

        while i < len(nums):
            counter, j = 1, 1
            while nums[i] + j in nums:
                j += 1
                counter += 1
            if counter > maximum:
                maximum = counter
            i += 1
        
        return maximum