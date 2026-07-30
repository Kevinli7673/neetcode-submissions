"""
Find elemement that appears size / 2 times
O(1) space O(n) time (no hashmap, no extra array)

Brute force: sorting then using counter
Time complexity: O(nlogn) 

Better solution: 
Using a hashmap - but this wouldn't work for the follow-up
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1
        
        for num in hashmap:
            if hashmap[num] > (len(nums)/2):
                return num
