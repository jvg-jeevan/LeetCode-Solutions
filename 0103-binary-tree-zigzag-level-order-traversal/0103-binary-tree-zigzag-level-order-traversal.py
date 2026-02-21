# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        res = []
        q = deque([root])
        count = 1

        while len(q) != 0:
            level_size = len(q)
            level = []

            for _ in range(level_size):
                node = q.popleft()
                level.append(node.val)
                
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            if count % 2 == 0:
                res.append(level[::-1])
            else:
                res.append(level)
            count += 1

        return res