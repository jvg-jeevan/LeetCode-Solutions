# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node, remaining, path):

            if node == None:
                return 
            
            # adding the node to path
            path.append(node.val)
            # subtracting from the target sum
            remaining -= node.val

            # checking if leaf node and equal to target sum
            if node.left == None and node.right == None and remaining == 0:
                res.append(path[:])

            # going till leaf
            dfs(node.left, remaining, path)
            dfs(node.right, remaining, path)

            # backtracking to remove the node if not reaching target sum
            path.pop()

        dfs(root, targetSum, [])

        return res