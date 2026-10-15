class Solution:
    def maxArea(self, heights: List[int]) -> int:

        i = 0
        j = len(heights) - 1


        max_area = 0
        while i < j:
            width = j - i
            height = min(heights[i], heights[j])
            area = width * height
            if area > max_area:
                max_area = area
                
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_area




# 2 8 3 4 8 9 2
# i
#             j


# insight is if you double pointer and work from outside in
# you are already starting with the largest possible "width"

        