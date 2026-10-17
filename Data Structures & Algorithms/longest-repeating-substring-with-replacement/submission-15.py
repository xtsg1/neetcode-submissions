#sliding window
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        longest = 1
        count = {}
        max_freq = 1
        L = 0
        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)
            max_freq = max(max_freq, count[s[R]])
            if (R - L + 1) - max_freq <= k:  #if valid replaceable
                longest = max(longest, (R - L + 1))
            else:
                count[s[L]] -= 1
                L += 1
        
        return longest

            

        
        

# A A A B B A B B 
#   L
#         R 
        