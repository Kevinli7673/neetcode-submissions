"""
This is removing a val from a linked list nth value from the end (not front)
For ex: if n = 5, we remove the 5th val from the end

Idea: We can iterate through the linked list first to find the length of it
Then we do length - n and find which element to remove
So when we get to the element before length - n, we make next point to the element
afterward

Issue: just realized that if we're gonna remove first element ts a problem
The idea is good, but what can i do in the code to make sure that it works
for every case, and not just for some

2nd idea: prob better
So the entire program is gonna be a while loop:
    set a dummy to move around 
    keep a counter


"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next

