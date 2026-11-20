# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# first attemp nov 20

# QUESTION
# what does it mean to invert a binary tree?
# i think it just means to swap left and right nodes
# but for every subsequent node also the left and right have to swap

# APPROACH
# im guessing we probably have to swap from bottom up, first invert the last things then come back up to invert
# base case is node is None
# then at each step we need a temp variable
# left to temp, right to left, temp to right i think
# or simply comma notation might work here for instataneous swap
# everything swaps in place
# at leaf nodes would the double Nones get swapped? does it matter? not sure about this if so it should be fine but idk about weird python quirks

# time: O(n) to traverse the tree
# space: O(1) because only scratch variable and pointers

class Solution:

    def swap(self, node: TreeNode) -> None:

        if node is None:
            return
        
        self.swap(node=node.left)
        self.swap(node=node.right)
        node.left, node.right = node.right, node.left


    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.swap(node=root)
        return root

        
        