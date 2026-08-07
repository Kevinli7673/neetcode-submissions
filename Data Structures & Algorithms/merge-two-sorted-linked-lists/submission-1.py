# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
first: find which list has the smaller initial value
Then we'll use a curr starting on that
We'll also have pointers for each list: and we iterate through the list
If one of the list is empty, we'll point curr to the other list 
If both are empty, return None
"""

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        temp = dummy

        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            
            temp = temp.next

        if list1:
            temp.next = list1
        elif list2:
            temp.next = list2

        return dummy.next