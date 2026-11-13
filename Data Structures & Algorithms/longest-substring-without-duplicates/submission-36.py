#rep nov 13

# QUESTION
# longest substring
# no dupes

# APPROACH
# sliding window starts with 2 pointers l,r
# window validity condition is no dupes
# how to do that?
# keep track of window
# determin if next character should be added
# or shrink current window
# keep track of longest ever seen

# if only one window slide through time is O(1)
# made need a set in worse case O(n) space

# walkthrough
#             6
# z x y z x y z
#       l
#             r

# " "

# window = z x y 

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        r = 0
        
        longest = 0
        window = ""
        while r <= len(s) - 1:

            if s[r] not in window:
                window += s[r]
                r += 1
            elif s[r] in window:
                l += 1
                window = window[1:] # pop leftmost char

            longest = max(longest, len(window))
            
        return longest
            





        