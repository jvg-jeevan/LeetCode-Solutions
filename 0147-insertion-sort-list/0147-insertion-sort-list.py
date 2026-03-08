# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        dummy = ListNode(0)
        cur = head
        while cur != None:
            prev = dummy
            while prev.next != None and prev.next.val < cur.val:
                prev = prev.next
            nxt = cur.next
            cur.next = prev.next
            prev.next = cur
            cur = nxt
        return dummy.next