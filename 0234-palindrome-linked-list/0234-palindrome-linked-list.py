# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return True
        
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        cur = slow
        prev = None
        while cur != None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        first = head
        second = prev

        while second != None:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True