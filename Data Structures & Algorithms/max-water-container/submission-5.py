# oct 31 rep

# QUESTION
# any 2 bars
# max storage
# wider container has more water
# height is the minimum of the two on the side
# return only amount (area)


# APPROACH
# two-pointer approach
# starting from the outside (max area)
# each pointer ticks inward > smaller one must decrement
# advantageous to keep the taller one whilt he other one decrements inwards
# store the maximum water area thus far


# WALKTHROUGH
# 1 7 2 5 4 7 3 6 
#   l           r

# 


class Solution:

    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1

        largest_area = 0

        while l < r:
            
            lh = heights[l]
            rh = heights[r]
            h = min(lh, rh)
            w = r - l
            a = h * w
            largest_area = max(largest_area, a)

            if lh <= rh:
                l += 1
            elif rh <= lh:
                r -= 1
        
        return largest_area

        