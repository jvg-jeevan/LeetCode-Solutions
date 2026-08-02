# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Find middle node using slow-fast pointers.
        # Middle becomes root.
        # Disconnect left half.
        # Recursively build left BST.
        # Recursively build right BST.

        def buildTree(node):
            
            if node == None:
                return None
                
            # for single node
            if node.next == None:
                return TreeNode(node.val)            

            slow = fast = node
            prev = None
            while fast != None and fast.next != None:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            root = TreeNode(slow.val)

            prev.next = None
            root.left = buildTree(node)
            root.right = buildTree(slow.next)

            return root

        return buildTree(head)