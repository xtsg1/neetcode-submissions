# GREEN 2026-11-25 | review, alone, first submit, 13:50, O(n)/O(1) correct | next review ~Jan
# nov 25 rep

#APPROACH
#maximum water is really the area of the water
#but its constrained by the outside bars
#has to be the lower of the two outside bars being checked
#and most likely the larger area is going to be on the most outside, longest
#so use two pointers right and left
#move from the outside in but how?
#at each loop calculate the area, store the biggest area found so far
#out of the two heights we need to move inwards whichever one is the smaller of the two
#because the larger one has the potential to form a bigger tub perhaps
#BECAUSE the larger one is not the LIMITING factor, the smaller one always is

# TIME: O(n) for 2 pointers
# MEMORY: O(1) should be area only and pointers

# WALKTHROUGH
# 1 7 2 5 4 7 3 6 
#   l         r

# solved in 13:50, a few typos self corrected

class Solution:

    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1

        largest = 0

        while l < r:

            lh = heights[l]
            rh = heights[r]
            h = min(lh, rh)  #taller one would overflow
            w = r - l
            area = int(w * h)
            largest = max(largest, area)

            # dynamically step inwards
            if lh <= rh:
                l += 1
            elif rh < lh:
                r -= 1
        
        return largest


            





        