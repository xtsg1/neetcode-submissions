# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# first attempt ever

# QUESTION
# binary tree
# we have root
# ordered traversal (from left to right?)

# APPROACH
# we need to use recursion
# this means calling the function from within the function (self-reference)
# but what are the operations of the function itself?
# we always need the leftmost
# so basically as long as the leftmost exists find it until the base case which is the node is None
# then back up one layer? loop? (unsure of language here) and record that output
# in this case append to list
# then check right side - but also recursively a second call because a rightside node could conceivably have yet another left child
# also can back up if None
# all very confusing but i think its ok

# Time: to traverse tree is O(nlogn)? unsure
# space: storage is only one new list so O(n)

# first time didn't time slowly worked it through with hints

class Solution:

    def iterate(self, node: Optional[TreeNode], res: List[int]):
        if not node:
            return
        self.iterate(node=node.left, res=res)
        res.append(node.val)
        self.iterate(node=node.right, res=res)


    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = [] 
        self.iterate(node=root, res=res)
        return res

    
        