# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None or n < 0:
            return None

        if head.next == None and n == 1:
            return None
        
        first = head
        second = head

        for _ in range(n):
            if first == None:
                return head
            first = first.next

        if first == None:
            return head.next

        while first.next != None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return head