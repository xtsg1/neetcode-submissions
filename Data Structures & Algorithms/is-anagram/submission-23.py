# GREEN review 2026-11-13 | 4:40, first try, O(n) time | space is O(1) for 26 lowercase letters (O(k) for k distinct chars), not O(n) | next review ~Dec 4
# rep nov 13

# QUESTION
# anagram
# means same count of letters

# APPROACH
# create a count dict for each string
# compare the two strings

# time O(n) if do each string at at time
# space O(n) for big dict in worst case

# SOLVED: 4m 40s

class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:


        s_count = {}
        for c in s:
            s_count[c] = s_count.get(c, 0) + 1

        
        t_count = {}
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1
        
        return s_count == t_count

