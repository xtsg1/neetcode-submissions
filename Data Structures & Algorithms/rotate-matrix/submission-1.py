# first attempt nov 16

# QUESTION
# rotate in place
# 90 degrees

# APPROACH
# using 3x3 as a base case
# start by transposing data across the main diagonal (0,0) (1,1) (2,2) etc
    # to do a transpose we swap the coordinates of all those to the top right of the diagonal (0,1) (0,2) (1,2)
    # columns are always row+1 to n (length of matrix)
# after transposing, the columns are just in the reverse order horizontally
    # so the columns need to be flipped
    # this means for each row we have to reverse the digits in that row
    

class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:

        n = len(matrix)

        # transpose
        for r in range(n): 
            for c in range(r+1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        # reversing each row
        for row in matrix:
            row.reverse()
        
        

        