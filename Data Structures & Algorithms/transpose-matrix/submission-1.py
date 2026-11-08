# first attempt nov 8

# QUES
# Transpose
# rows become columns
# columns become rows

# APPROACH
# [[row], [row], [row]]

class Solution:

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        cols = []

        for c in range(len(matrix[0])): # of cols

            col = []
            for r in matrix:
                col.append(r[c])
            
            cols.append(col)
        
        return cols
            
        