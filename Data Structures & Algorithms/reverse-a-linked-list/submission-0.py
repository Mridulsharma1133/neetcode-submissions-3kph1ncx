# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Prev, Curr = None, head

        while Curr:
            nxt = Curr.next
            Curr.next = Prev
            Prev = Curr
            Curr = nxt
        
        return Prev
        