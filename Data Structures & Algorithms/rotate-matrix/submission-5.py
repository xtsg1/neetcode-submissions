# GREEN 2026-11-22 | cold, alone, first submit, 10:10 | time is O(n^2) for an n x n grid (every cell is touched), space O(1) | review ~Dec 13
# rep nov 22

# APPROACH
# the shape of the solution is transpose across diagonal + all rows get inverted
# Transpose
    # To transpose, we need to swap 2,3,6 against 4,7,8. specifically swapping to their complement i,j <> j,i
    # in a 3x3
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # to loop this we can skip the value of the diagonal itself and go to end so start j+1 something like that
# Invert
    # for each row
    # reverse the list

# time: transposing would be nested loops but not all n objects are accessed, reversal is just O(n) 
# space: everything is swapped in place so extra space is only pointers O(1)


# SOLVED: in 10:10 but didn't feel so much as learning just felt like i "knew" the trick this time idk man i still dont think i ever would have figured out this geometry cold ._. 

class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:

        # transpose
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):  # skip diagonal
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # reverse
        for r in matrix:
            r.reverse()
        



