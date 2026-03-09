from math import pow

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        cur = head
        prev = None
        while cur != None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        cur = prev

        num = 0
        i = 0
        while cur != None:
            num += (cur.val * int(pow(2, i)))
            cur = cur.next
            i += 1
        return num