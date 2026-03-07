# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return head

        n = 0
        node = head
        while node != None:
            node = node.next
            n += 1
        
        k = k % n

        for _ in range(k):
            cur = head
            while cur.next.next != None:
                cur = cur.next
            node = cur.next
            cur.next = None
            node.next = head
            head = node
        return head