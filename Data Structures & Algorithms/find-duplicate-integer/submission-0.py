"""
We're finding a duplicate in a array only using O(1) extra space
n is the biggest val in the array and the array can only contain n + 1 vals

What if we use the values at the index as a indice
because since length is n + 1 the biggest val is gonna be the last index
We can use fast and slow pointers to find the duplicate
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        fast = 0
        slow = 0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break
        
        slow1 = 0

        while slow1 != slow:
            slow = nums[slow]
            slow1 = nums[slow1]
            
        return slow1