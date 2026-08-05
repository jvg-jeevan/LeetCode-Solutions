# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return 0

# get the left and right side depth
        left_side = self.minDepth(root.left)
        right_side = self.minDepth(root.right)

# this is because if skewed to one side it should not give only root as depth
# if left side is null take right and viceversa
        if left_side == 0:
            return 1 + right_side

        if right_side == 0:
            return 1 + left_side

        return 1 + min(left_side, right_side)
