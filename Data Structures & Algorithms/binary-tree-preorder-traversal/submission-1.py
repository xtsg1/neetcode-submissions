# GREEN 2026-11-18 | cold, first try, 10:00; first cold tree solve | O(n) time right | space: O(n) output + O(h) recursion stack | nit: helper returns res but nobody uses it; return nothing or use the value | next review ~Dec 9
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# first attempt

# APPROACH
# preorder traversal - what does this even mean
# so we record node itself before we do child nodes
# but for child nodes we would do the left first
# and then right as well
# output normal list
# base case is a None node

# time: traversal only so O(n)
# space: only a list so O(n)

# solved: omg omg i did it in 10 minutes flat first time?!?!?!?!?!

class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def go(node: Optional[TreeNode], res: List[int]) -> List[int]:
            
            if not node:
                return res
            
            res.append(node.val)
            go(node=node.left, res=res)
            go(node=node.right, res=res)

            return res

        res = [] 
        go(node=root, res=res)
        return res
        






        