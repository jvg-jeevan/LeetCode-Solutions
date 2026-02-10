# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None
        slow = head
        fast = head

        # go to point where they meet and store in fast
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                break

        else:
            return None
        
        # slow start from head and go until they meet and retunn the node
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow