class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [1], [1] * len(nums)
        output = []
        for i in range(len(nums)):
            if i != 0:
                left.append(nums[i-1] * left[i-1])

        for i in range(len(nums) - 1, -1, -1):
            if i!=len(nums)-1:
                right[i] = right[i+1] * nums[i+1]

        for i in range(len(nums)):
            output.append(left[i] * right[i])
        return output