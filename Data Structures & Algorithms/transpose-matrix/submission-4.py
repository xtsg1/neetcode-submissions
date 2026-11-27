# GREEN 2026-11-27 | review, 4:08, first submit | complexity: O(m*n) time and space | next ~Dec 18
# rep  nov 27


# APPROACH
# so a transpose means every row becomes a colum and vice versa
# so grab each col (tricky one)
# make anew matrix where each col is the row
# done

# time: O(n), because scales with however many columns
# space: O(n) also creating a new matrix as its happening

# solved: 4:08


class Solution:

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        transposed = []
        for col in zip(*matrix):
            transposed.append(col)
        
        return transposed

        