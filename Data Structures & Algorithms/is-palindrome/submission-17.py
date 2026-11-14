# YELLOW review 2026-11-14 | 15:22, two pointers right; hints: l < r guard on the inner skip loops, l == r check was wrong (odd palindromes) | complexity: O(n) time, O(1) space | redo ~Nov 18
# rep nov 14

# QUESTION
# palindrome same forward backward
# return true false only
# ignore non alphanumerics

# APPROACH
# two pointers start from both ends
# check that they match
# skip non alphanumeric


# solved needed logical hint on l<r check on inner loop
# 15:22s

class Solution:

    def isPalindrome(self, s: str) -> bool:

        l = 0
        r = len(s) - 1

        while l < r:

            while not s[l].isalnum() and l < r: #fast forward not alphanumeric chars
                l += 1
            while not s[r].isalnum() and l < r:
                r -= 1
            
            if s[l].lower() != s[r].lower(): #non equivalent means invalid
                return False
            
            l += 1  #increment/decrement normally
            r -= 1 

         
        return True
                
# Madam, in Eden, I'm Adam


        