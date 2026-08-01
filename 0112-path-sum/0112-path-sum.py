# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

# dfs is used to find the sum of the path
        def dfs(node, cur):    
            if node == None:
                return False
# storing sum of each path
            cur = cur + node.val
# if leaf node comparing with targetSum
            if node.left == None and node.right == None:
                return cur == targetSum
# or is used, even one case is true then rest is true
            return dfs(node.left, cur) or dfs(node.right, cur)

        return dfs(root, 0)