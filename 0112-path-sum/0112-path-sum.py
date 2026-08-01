# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        res = []

        def dfs(node, cur):    
            if node == None:
                return None        
            cur = cur + node.val

            if node.left == None and node.right == None:
                res.append(cur)

            dfs(node.left, cur)
            dfs(node.right, cur)

       
        dfs(root, 0)

        print(res)
        return targetSum in res