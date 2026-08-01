class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = defaultdict(list)

        for i in range(len(nums)):
            hashmap[nums[i]].append(i)
        
        for i in range(len(nums)):
            if target-nums[i] in hashmap:
                for val in hashmap[target-nums[i]]:
                    if val != i:
                        return [i, val]
                
