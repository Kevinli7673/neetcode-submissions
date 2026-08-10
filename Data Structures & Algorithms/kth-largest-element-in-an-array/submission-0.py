"""
Idea: we heapify and pop for k amt
then return array[0]
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums = [-s for s in nums]

        heapq.heapify(nums)

        for i in range(k):
            res = heapq.heappop(nums)
        
        return -res