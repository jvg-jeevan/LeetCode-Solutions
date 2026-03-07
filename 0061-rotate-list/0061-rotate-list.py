# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        n = 1
        tail = head
        while tail.next != None:
            tail = tail.next
            n += 1

        k = k % n
        if k == 0:
            return head
        
        tail.next = head

        steps = n-k-1
        new_tail = head
        for _ in range(steps):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        
        return new_head



        # if head == None:
        #     return None
        # if head.next == None:
        #     return head

        # n = 0
        # node = head
        # while node != None:
        #     node = node.next
        #     n += 1
        
        # k = k % n

        # for _ in range(k):
        #     cur = head
        #     while cur.next.next != None:
        #         cur = cur.next
        #     node = cur.next
        #     cur.next = None
        #     node.next = head
        #     head = node
        # return head