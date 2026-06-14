class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i, num in enumerate(nums):
            difference = target - num
            if difference in nums and i != nums.index(difference):
                index = nums.index(difference)
                if(i > index):
                    return [index, i]
                else:
                    return [i, index]