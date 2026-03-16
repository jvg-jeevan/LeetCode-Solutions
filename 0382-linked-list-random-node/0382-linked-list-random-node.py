# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#        self.next = next

import random 

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        res = self.head.val
        node = self.head.next
        i = 2
        while node != None:
            if random.randint(1, i) == 1:
                res = node.val
            node = node.next
            i += 1
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()