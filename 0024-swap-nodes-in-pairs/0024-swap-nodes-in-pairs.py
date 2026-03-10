# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        cur = head.next.next
        prev = head
        head = head.next
        head.next = prev

        while cur != None and cur.next != None:
            prev.next = cur.next
            prev = cur
            nxt = cur.next.next
            cur.next.next = cur
            cur = nxt
        prev.next = cur
        return head