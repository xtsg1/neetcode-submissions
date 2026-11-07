## rep nov 7

# Question
# find substring such that no character is a duplicate of the substring
# contiguous

# Approach
# use a valid window
# validity condition - next character must not be in the substring
    # can increment
    # otherwise decrement left side of window
# substring always gets compared with max if its valid
# at the end the right pointer hits len-1 
# and it must be a valid window
# or l AND r both hit th end


# Stepthrough
# z x y z x y
#       l
#           r

# window: z x y
# longest: 3

# solved in 25_ minutes
# required failed on performance because used list instead of set
# figured out set later


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0
    
        longest = 0
        l = 0
        r = 0
        window = set()

        while True:

            if s[r] not in window:   #valid increment
                window.add(s[r])
                length = len(window)
                longest = max(longest, length)
                if r == len(s) - 1:
                    break
                r += 1

            elif s[r] in window:
                window.remove(s[l])  # rm leftmost element
                l += 1

        return longest







                

