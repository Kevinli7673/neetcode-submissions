"""
Breakdown: We have a regular linked list
           The only difference is that the last element doesn't point to Null
Check if the linked list is going in circle

edge case: 
Check if the linked list is longer than one val

Idea: 
We can have a loop that goes for 1001, this is because of the constraint
length of list <= 1000, and worse scenario so we can check if next is null or not
Issue: This is tech O(1) but slower than other O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
