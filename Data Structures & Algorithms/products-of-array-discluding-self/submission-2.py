class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = []
        total = 1
        totalwithout0 = 1

        hashmap = defaultdict(int)

        for val in nums:
            total = total * val
            hashmap[val] += 1
        
        if hashmap[0] and hashmap[0] < 2:
            for val in nums:
                if val != 0:
                    totalwithout0 = totalwithout0 * val
            
            for val in nums:
                if val != 0:
                    res.append(0)
                else:
                    res.append(int(totalwithout0))
            
        
        if hashmap[0] and hashmap[0] >= 2:
            for val in nums:
                res.append(0)
        
        if not hashmap[0]:
            for val in nums:
                res.append(int(total/val))
        

        return res
        


