# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        # dfs is used to go along depth
        def dfs(node, current):
            
            if node == None:
                return 0
            # to calculate the current value i.e 1 * 10 + 3
            current = current * 10 + node.val

            # if it is a leaf node return the current value
            if node.left == None and node.right == None:
                return current

            # check for left and right subtree
            return dfs(node.left, current) + dfs(node.right, current)

        return dfs(root, 0)