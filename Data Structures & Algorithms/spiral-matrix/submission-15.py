# RED 2026-11-24 | own approach, hints on directions list + check next square, final loop given | redo ~Nov 26
# first attempt

# APPROACH
# ok lets see for a 2x2
# the order of spiral traversal will always be Right, Down, Left, Up, in that order
# if we hit an edge we traverse in one of the other directions in that order
# keep track of every coordinate we've seen as a set(tuple())
# if we hit an edge swithc directions
# if we hit a previously seen box switch directions

# time: O(1) every element accessed once
# space: O(n) multiple lists are needed but not exponentially

# 50 minutes with lots of ai help to debug

class Solution:


    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        turns = [
            (0,1),     #R  0
            (1,0),     #D  1
            (0,-1),    #L  2
            (-1,0),    #U  3
        ]

        nrow = len(matrix)
        ncol = len(matrix[0])
        nsquares = nrow * ncol
        r, c = 0, 0
        orient = 0
        seen = set()
        res = []

        while len(seen) < nsquares:
            n = matrix[r][c]
            seen.add((r, c))
            res.append(n)

            nr = r + turns[orient][0]
            nc = c + turns[orient][1]

            if not (0 <= nr < nrow and 0 <= nc < ncol) or (nr, nc) in seen:
                orient = (orient + 1) % 4
                nr = r + turns[orient][0]
                nc = c + turns[orient][1]
            
            r, c = nr, nc #always step

        return res 
        


            











            





        
        