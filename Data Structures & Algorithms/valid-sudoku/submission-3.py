# YELLOW 2026-11-11 | hint: box top-left corners + walk the 3x3; range syntax | complexity: O(n^2) for an n x n board (O(1) for fixed 9x9), O(n) space | redo ~Nov 15
# rep Nov 11

# QUESTION
# each 3x3 must have 1-9 no dupes
# each row no dupes
# each col no dupes

# APPROACH
# need to figure out easy way to get no dupes first
# can use old trick of len(set(x)) == len(x)
# to deal with . we can do set.remove?
# first do rows
# then do cols
# then how to do 3x3s?

# FINISHED: 25m + with multiple syntactical hints as well as 3x3 grid approach not familiar with base python matrices really annoyed and frustrated

class Solution:

    def dupe(self, x):
        nums = [n for n in x if n != "."] #rm .
        if len(set(nums)) != len(nums):
            return True
        return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # rows first
        for row in board:
            if self.dupe(row):
                return False
        
        # cols O(n^2)
        for i in range(len(board[0])):
            col = []
            for row in board:
                col.append(row[i])
            if self.dupe(col):
                return False

        for col in range(0, 9, 3): # stepsize 3
            for row in range(0, 9, 3):
                block = []
                for r in range(row,row+3):
                    for c in range(col,col+3):
                        block.append(board[r][c])
                        if self.dupe(block):
                            return False
        return True
                    






        