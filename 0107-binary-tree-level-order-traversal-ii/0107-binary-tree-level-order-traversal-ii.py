from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
# to store the result nodes
        result = []
# to keep track of the nodes not visited
        q = deque([root])

        while q:
# to get each levels
            level = []
            level_size = len(q)

# pop a node from q and add to level and check whether node has left or right if yes then add to q 
# in this level size gives like the unvisited node at each level
            for _ in range(level_size):
                node = q.popleft()
                level.append(node.val)

                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)

            result.append(level)

        return result[::-1]