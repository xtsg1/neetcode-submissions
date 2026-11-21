# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# after chatting with coach will attempt a second solution

class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dig(node: TreeNode) -> int:

            if node is None:
                return 0
            
            lh = dig(node=node.left)
            rh = dig(node=node.right)
            h = max(lh, rh)
            h += 1  #my own height
            return h
        
        d = dig(node=root)
        return d
        