class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1 
        counter = len(nums)

        while(l <= r):
            if nums[l] == val:
                counter -= 1
                while nums[r] == val and l < r:
                    nums[r] = 0
                    r -= 1
                    counter -= 1
                nums[l] = nums[r]
                r -= 1
            l += 1
        print(nums)
        return counter