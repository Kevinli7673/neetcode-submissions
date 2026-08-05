# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Steps: 
1. We have top pointers, both on the first element of their linked list
2. Check if the left value is >= right value
    if so:
        the right value is gonna be head
    else:
        left value becomes head

3. While loop: Until both pointers get to null:
    which if left value is >= r:
        the head points to right value (we have to save the left.next so we can 
                                        access it later to compare agin)
    else (means l < r):
        the head points to the current left pointer:
        if the head was right pointer (than we have to save right.next)
    
    return res (gonna be the head)

Another idea that might help:
We have 2 temp pointers that are pointer.next so we can access the next val
and we can change the pointers without a issue and reassign the pointers
to the temp pointers and move temp pointers
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next