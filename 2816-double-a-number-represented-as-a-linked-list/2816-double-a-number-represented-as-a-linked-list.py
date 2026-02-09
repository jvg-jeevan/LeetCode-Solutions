# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(head):
            cur = head
            prev = None
            while cur != None:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev
        
        head = reverse(head)

        carry = 0
        cur = head
        while cur != None:
            total = cur.val * 2 + carry
            cur.val = total % 10
            carry = total // 10
            cur = cur.next
        
        if carry != 0:
            new_node = ListNode(carry)
            cur.next = new_node

        return reverse(head)