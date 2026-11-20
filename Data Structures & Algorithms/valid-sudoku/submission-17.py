# YELLOW 2026-11-20 | box corners alone; hints: dupe filter (new list, not remove-in-loop), range(j, j+3) typo | ~40 min | redo ~Nov 24
# rep nov 20

# QUESTION
# each row 1-9 no dupes
# each column 1-9 no dupes
# each 3x3 no dupes

# APPROACH
# probably need a simple reusable check dupe function
# remove dots, set() the input, check if input length is same as input length
# do that for each row
# do that for each column
# how to do 3x3 squares?
# first loop through 0,3,6 (the start of boxes)
# within each one loop through n+0 n+1 n+2
# but have to do it for columns and rows so O(n^4) ?!?!?!
# what....


# solved, needed lots of hints, but figured out the 3x3 myself. needed 25m+++ 

class Solution:

    def dupe(self, inp: List[str]) -> bool:

        rm = []
        for c in inp:
            if c != ".":
                rm.append(c)

        if len(set(rm)) == len(rm):
            return False

        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            if self.dupe(inp=row):
                return False
        
#        for i in range(len(board[0])):
#            col = []
#            for row in board:
#                col.append(row[i])
#            if self.dupe(col):
#                return False

        for col in zip(*board):
            col = list(col)
            if self.dupe(inp=col):
                return False
        
        for i in [0,3,6]:
            for j in [0, 3, 6]:

                block = [] 
                for r in range(i, i+3): 
                    for c in range(j, j+3):
                        block.append(board[r][c])
                
                if self.dupe(block):
                    return False

        # passes all three
        return True
                        

        
        