# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def checkDFS(node, low, high):
            if node == None:
                return True

            if node.val <= low:
                return False

            if node.val >= high:
                return False

            return (checkDFS(node.left, low, node.val) 
                and 
                checkDFS(node.right, node.val, high))

        return checkDFS(root, float('-inf'), float('+inf'))