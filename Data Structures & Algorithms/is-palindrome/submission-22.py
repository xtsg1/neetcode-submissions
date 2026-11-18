# GREEN review 2026-11-18 | cold, alone, 5:25, first try (Nov 14: 15:22 with hints) | one loop, if/continue skips, single l < r guard | O(n) time, O(1) space both right | nit: skip NON-alphanumeric chars | next review ~Dec 9
# rep nov 18

# APPROACH

# two pointers
# count from both sides
# pointers never cross
# alphanumeric characters must be skipped

# walkthrough

# Was it a car or a cat I saw?

# time: O(n) everything looped once
# space: O(1) only pointers 

# solved: 5m 25s

class Solution:

    def isPalindrome(self, s: str) -> bool:

        l = 0
        r = len(s) - 1

        while l < r:
            
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True
        