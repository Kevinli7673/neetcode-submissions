class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        max = 0

        for num in hashset:
            counter = 1
            while num+1 in hashset:
                counter += 1
                num += 1
            if counter > max:
                max = counter
        return max
            