class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maximum = 0

        for num in nums:
            i = 1
            counter = 1
            while num + i in nums:
                counter += 1
                i += 1
            if counter > maximum:
                maximum = counter
        
        return maximum