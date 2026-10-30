class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        seen = set()
        res = []

        def recursion(nums, curr, seen):
            i = 0
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            while i < len(nums):
                if(nums[i] not in seen):
                    seen.add(nums[i])
                    curr.append(nums[i])
                    recursion(nums, curr, seen)

                    seen.remove(nums[i])
                    curr.pop()
                i += 1
        
        recursion(nums, [], seen)
        return res