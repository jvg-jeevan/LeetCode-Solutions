# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next == None:
            return head

        # finding middle
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second half
        cur = slow.next
        slow.next = None # breaking list
        prev = None
        while cur != None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        first, second = head, prev
        while second != None:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2