# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        track = []

        curr = head
        while curr:
            track.append(curr)
            curr = curr.next
        
        
        if len(track) - n == 0:
            head = head.next
            return head
        else:
            remove = track[len(track) - n]
            prev = track[len(track) - n - 1]
            prev.next = remove.next
            return head

        