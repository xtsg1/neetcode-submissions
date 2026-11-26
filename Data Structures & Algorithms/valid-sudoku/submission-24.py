# rep nov 26

# APPROACH
# need a helper function to find dupes
    # first remove .
    # then check set lenght equal to list length
# then first do rows
# then do columns
# for blocks:
    # loop through 0,3,6 outer
    # inner loop 0,1,2
    # create the block
    # run block through helper

# time: O(n^2)
# space: O(n) making extra rwos/blocks

# solved in 16:20 wiht hint on column idiom zip(*board) which i need to spaced repetition

class Solution:

    def dupe(self, inp: List) -> bool:

        nums = [] #rm .
        for c in inp:
            if c != ".":
                nums.append(c)
        
        if len(set(nums)) < len(nums):  #if shorter, then dupes exist
            return True
        return False


    def isValidSudoku(self, board: List[List[str]]) -> bool:


        for row in board:
            if self.dupe(inp=row):
                return False

        for col in zip(*board):
            if self.dupe(inp=col):
                return False
        
        # build the blocks
        
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                block = []
                for r in [0, 1, 2]:
                    for c in [0, 1, 2]:
                        block.append(board[i+r][j+c])
                if self.dupe(inp=block):
                    return False
        
        return True

            
        




            
        