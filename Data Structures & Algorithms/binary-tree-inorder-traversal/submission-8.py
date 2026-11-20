# GREEN 2026-11-20 | cold, alone, first try, 11 min | add O(n) time / O(h) stack line | review ~Nov 27
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# QUESTION
# inorder = means the leftmost node always gets read first

# APPROACH
# starting from the root
# we traverse left until we get to the bottom
# this is recursive
# the base case is None node
# the order is left recursive, ?middle?, right recursive
# in example tree the traversal should be: 1 2 4 None 4 None 2 5 None 5 None 1 ...
# where none are the base cases of left/right recursives


# Solved Cold in 11m

class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def move(node: TreeNode, res: List[int]) -> List[int]:

            if not node:  # base case up one level
                return
            
            move(node.left, res=res)
            res.append(node.val)
            move(node.right, res=res)  # right always last
        
        res = []
        move(node=root, res=res)
        return res

        



        