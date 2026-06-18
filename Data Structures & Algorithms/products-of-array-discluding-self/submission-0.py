class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        output = []
        for i in range(len(nums)):
            right = 1
            if i != 0:
                left *= nums[i-1]
            for j in range(i+1, (len(nums))):
                right *= nums[j]
            output.append(right * left)
        return output
