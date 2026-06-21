"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        track = {None: None}
        curr = head
        res = start = Node(0)

        while curr:
            track[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            track[curr].next = track[curr.next]
            track[curr].random = track[curr.random]
            curr = curr.next
        return track[head]
        
        