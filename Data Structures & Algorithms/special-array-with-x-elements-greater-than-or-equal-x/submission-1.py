class Solution:
    def specialArray(self, nums: List[int]) -> int:
        """
        We initiate a map that stores [nums[i]] : amt of it
        then we run a for loop for 1 to len of nums
        then we add up all the value in hashmap that is bigger than
        i
        
        """
        map = defaultdict(int)
        for n in nums:
            map[n] += 1
        
        for i in range(1, len(nums)+1):
            total = 0
            for key in map:
                if i <= key:
                    total += map[key]
            
            if(i == total):
                return i
        
        return -1




