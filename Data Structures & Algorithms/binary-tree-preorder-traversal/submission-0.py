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
        






        