"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

"""
Deep copy: Everytime i hear this its mostly likely hashmap
What we do is create a hashmap with [node] : next, random
While dummy, we add each node to the hashmap, however we don't add random pointer until the 2nd
time because it might be pointing at a node that we haven't created yet
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None


        copy = dict()
        dummy = head

        while dummy:
            copy[dummy] = Node(dummy.val)
            dummy = dummy.next
        
        dummy = head
        
        while dummy:
            copy[dummy].next = copy.get(dummy.next)
            copy[dummy].random = copy.get(dummy.random)
            dummy = dummy.next
        
        return copy.get(head)