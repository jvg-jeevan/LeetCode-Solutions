# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        # using inorder traversal 
        # res to store final result
        # count to take current node value count as BST and inorder occurrences will be consecutive
        # max_count to keep track of mode once a node to found to be maximum occurrence the other nodes with same occurrence can also be added
        # prev to keep track of prev visited node to increment count

        res = []
        count = 0
        max_count = 0
        prev = None

        def inorder(node):
            nonlocal res, count, max_count, prev           
            
            if node != None:
                inorder(node.left)

                if prev == node.val:
                    count += 1 
                else:
                    count = 1

                if count > max_count:
                    max_count = count
                    res = [node.val]
                
                elif count == max_count:
                    res.append(node.val)
                    
                prev = node.val

                inorder(node.right)

        inorder(root)

        return res