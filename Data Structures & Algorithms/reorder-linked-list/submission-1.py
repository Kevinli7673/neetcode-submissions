# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Idea: we find the middle of the linked list
Then we reverse the 2nd part of the linked list
Then we can start from the first element and the middle pointer 

How to reverse from middle 
we have to save the node before the middle
then we can a dummy node = prev
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        m = curr = slow.next
        prev = None
        temp = curr
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        slow.next = None
        
        dummy = head
        while prev:
            temp = dummy.next
            temp2 = prev.next

            dummy.next = prev
            prev.next = temp
            dummy = temp
            prev = temp2
        


