# sliding window


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest = 0
        window = set()

        l = 0
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            longest = max(longest, len(window))
        
        return longest



# z x y z x y z
# 
#     l---r
#       
        