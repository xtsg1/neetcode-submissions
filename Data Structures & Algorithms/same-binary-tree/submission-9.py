# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# QUESTION
# roots of two binary trees
# return tree if and only if three are equivalent?
# equivalence means same structure and same node values...

# APPROACH
# so my thought is to traverse both trees at the same time
# a recursive function that steps both trees in the same direction and same order
# base case is still Node is None
# values are easy to compare with equivalence
# but what about different tree structure?
# if one side has extra nodes what happens? if one side has extra node and the other doesnt one side just roll back up and compare the wrong value which results in false
# what must be promised by each layer? 
# we need to promise that both trees are stepping simultaneously, not one after another
# check values are equivalent
# how do i return True in a recurisve method?

# time: traversal should be O(n)
# space: O(h)


class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def equivalence(p: TreeNode, q: TreeNode) -> bool:

            if p is None and q is None:
                return True
            elif p and q is None:  #xor?
                return False
            elif q and p is None:
                return False
            
            # traverse all the way before checking 
            left_eq = equivalence(p=p.left, q=q.left)
            right_eq = equivalence(p=p.right, q=q.right)

            if (not left_eq) or (not right_eq):
                return False
            if p.val != q.val:
                return False

            return True # the top layer return?? a little fuzzy here

        equal = equivalence(p=p, q=q)
        return equal


