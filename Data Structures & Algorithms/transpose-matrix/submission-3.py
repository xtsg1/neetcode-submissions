# rep  nov 27


# APPROACH
# so a transpose means every row becomes a colum and vice versa
# so grab each col (tricky one)
# make anew matrix where each col is the row
# done

# O(n), because scales with however many columns


class Solution:

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        transposed = []
        for col in zip(*matrix):
            transposed.append(col)
        
        return transposed

        