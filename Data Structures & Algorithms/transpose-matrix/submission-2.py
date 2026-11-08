# GREEN 2026-11-08 | first try | complexity: O(m*n) time, O(m*n) space for the output
# first attempt nov 8

# QUES
# Transpose
# rows become columns
# columns become rows

# APPROACH
# [[row], [row], [row]]

# double loop
# time O(n^2)
# space O(n) only a list of fixed lengths created


class Solution:

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        cols = []

        for c in range(len(matrix[0])): # of cols

            col = []
            for r in matrix:
                col.append(r[c])
            
            cols.append(col)
        
        return cols
            
        