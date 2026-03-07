# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dummy if head also has duplicates
        dummy = ListNode(0)
        dummy.next = head
        # prev and cur nodes to track
        prev = dummy
        cur = head       

        while cur != None:
# get the duplicate value
            if cur.next != None and cur.val == cur.next.val:
                value = cur.val
# remove all nodes with duplicate values
                while cur != None and cur.val == value:
                    cur = cur.next
# update prev node with cur value without duplicate
                prev.next = cur
# if no duplicates update
            else:
                prev = prev.next
                cur = cur.next
        
        return dummy.next