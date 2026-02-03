# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)
        dummy = ListNode(0)
        dummy.next = head
        
        cur = dummy
        while cur.next != None:
            if cur.next.val in nums_set:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next