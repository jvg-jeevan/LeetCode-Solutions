# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)
        if root == None:
            return new_node

        cur = root

        while cur != None:
            parent = cur
            if cur.val == val:
                return root
            elif cur.val > val:
                cur = cur.left
            else:
                cur = cur.right
        
        if parent.val < val:
            parent.right = new_node
        else:
            parent.left = new_node

        return root