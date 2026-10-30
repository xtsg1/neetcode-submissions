# Oct 30 rep

# APPROACH
# anagrams just means they contain the same characters the same number of times
# a hashmap of the characters and how often they appear
# to do that we need to loop through each string once
# do that for both strings 
# still O(n)
# check equivalency of the dictionaries


class Solution:

    def isAnagram(self, s: str, t: str) -> bool:


        s_count = {}
        for c in s:
            s_count[c] = s_count.get(c, 0) + 1
         
        
        t_count = {}
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1
        
        if s_count == t_count:
            return True  # is anagram
        return False