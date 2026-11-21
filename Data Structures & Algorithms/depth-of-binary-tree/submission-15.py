# GREEN 2026-11-21 | first sight, alone, first submit, 23:35 | space is O(h); h -= 1 not needed (each call has its own h); try return 1 + max(left, right) | review ~Nov 28
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# first attempt

# APPROACH
# find depth (h)
# so again recursion
# base case is Node is None
# how to keep track of depth when popping down and back up?
# h += 1 at start of method, upon return h -=1 ? not sure but we can try it
# then keep a running tally of deepest?
# traverse leftfirst, then self? 

#this is tricky it hingest on keeping some kind of state of each level of recursion but within that layer

# time: traversal is O(n)
# only store pointers, but at each layer or recursion means its O(n) or O(logn)? cant remember

# solved: 23:35
#had trouble with variable scope, initially deepest was not modifying in place like i expected it to, i had to return it each time, not the same for lists
# each time coming back up the stack i had to return the deepest found 
# and pass that into the next call to keep digging 
# previously using a list can modify in place but variables are difference? could use guidance on this python behaviour

class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dig(node: TreeNode, h: int, deepest: int):

            if node is None:
                return deepest
            
            h += 1 # count self
            print(f"h{h}")
            deepest = max(deepest, h)
            print(f"d{deepest}")
            deepest = dig(node=node.left, h=h, deepest=deepest)
            deepest = dig(node=node.right, h=h, deepest=deepest)
            h -= 1

            return deepest #had trouble with variable scope, initially deepest was not modifying in place like i expected it to, i had to return it each time, not the same for lists
        
        h = 0
        deepest = 0
        deepest = dig(node=root, h=h, deepest=deepest)

        return deepest

        
        





        