# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# first attempt

# QUESTION
# basically does EXACTLY subroot EXISIT within ROOT
# same node/descendants and values

# APPROACH
# traverse normally, check self, then left, then right
# check if self value is same as subroot's ROOT node
# if so its a candidate to test
# begin traversing subroot simultaneously. how?'
    # 2nd function?
    # check equivalency recursion function?
# check at each stage root == subroot recursively
# but duplicates means we have to keep going until we find another matching val
# only at the very end we can return False
# recursion: what is the one promise of each layer?
# Am I equivalent to subroot 


class Solution:   

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def equivalent(node: Optional[TreeNode], subnode: Optional[TreeNode]):

            if (node and not subnode) or (subnode and not node):
                return False
            elif not node and not subnode:
                return True

            left = equivalent(node=node.left, subnode=subnode.left)
            right = equivalent(node=node.right, subnode=subnode.right)

            if node.val != subnode.val:
                return False
            
            if not (left and right):
                return False
            
            return True



        
        def traverse(node: Optional[TreeNode], subnode: Optional[TreeNode]):

            if node is None:
                return
            
            if node.val == subnode.val:
                if equivalent(node=node, subnode=subnode):
                    return True
                
            
            left = traverse(node=node.left, subnode=subnode)
            right = traverse(node=node.right, subnode=subnode)

            if left or right:
                return True
            else:
                return False
        
        return traverse(node=root, subnode=subRoot)
        