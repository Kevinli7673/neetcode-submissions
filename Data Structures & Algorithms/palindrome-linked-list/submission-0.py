# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        we find the length of the linked list
        then we find the middle and reverse it
        then we can compare from the front and the middle of the linked
        list
        """

        length = 0
        dummy = head

        while dummy:
            dummy = dummy.next
            length += 1
        
        dummy = head

        mid = math.ceil(length/2)
        i = 0

        while i != mid:
            dummy = dummy.next
            i += 1
        
        prev = None
        while dummy:
            temp = dummy.next
            dummy.next = prev
            prev = dummy
            dummy = temp

        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next

        return True
