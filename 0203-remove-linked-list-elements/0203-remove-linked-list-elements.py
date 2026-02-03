# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # attach extra dummy node to the head
        dummy = ListNode(0)
        dummy.next = head

        # traverse until last node using dummy
        cur = dummy
        while cur.next != None:
            # if val same then attach current next value by skipping the node to be deleted
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        # dummy.next is returned as dummy to be ignored
        return dummy.next