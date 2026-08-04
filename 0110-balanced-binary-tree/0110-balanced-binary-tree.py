# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # bottom up dfs approach 
        # like taking height of the tree from bottom 
        # node will return the height if abs(left - right) > 1 then false

        def height(node):

            if node == None:
                return 0

            left = height(node.left)

            if left == -1:
                return -1
            
            right = height(node.right)

            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        return height(root) != -1