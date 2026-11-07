# nov 7 first try

# QUESTION
# valid palindrome
# same forward and backward
# but can delete 1 character to make it valid
# or not!
# at most 1 deletion


# APPROACH
# two pointers from both side
# check equivalence
# if not check which side to "delete" i/j +- 1 must be equal
# track deletion charges (bool)
# if deletion charges are all used and more inequality then also fail

# twopointer O(n) time
# only pointers nad deletion tracker O(1) space


# walk
# e c e e c 
#   l    
#         r

class Solution:

    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
        

    def validPalindrome(self, s: str) -> bool:

        l = 0
        r = len(s) - 1 

        deleted = False

        while l < r:

            if s[l] != s[r]:
                if deleted:
                    return False
                else:
                    left = s[l:r]
                    right = s[l+1:r+1]
                    return self.isPalindrome(s=left) or self.isPalindrome(s=right)

            l += 1
            r -= 1
        
        return True
                    

        