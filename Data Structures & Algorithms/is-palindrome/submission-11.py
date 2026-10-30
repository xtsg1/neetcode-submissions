# oct 30 rep

# APPROACH
# palindrome basically means mirror across the middle
# we can do two pointers from either end
# check equivalency of left and right pointers
# move em both each iteration
# since every element is accessed once thats O(n) time
# for space would be O(1) because only two pointers of memory


# WALKTHROUGH
# tab a cat
# l       r
# if not same then fail
# if same both step
# if left not alphanum then only left stpes
# same for right

class Solution:

    def isPalindrome(self, s: str) -> bool:
        
        l = 0
        r = len(s) - 1

        while l < r:

            if s[l].isalnum() and s[r].isalnum():
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1

            if not s[l].isalnum():
                l += 1

            if not s[r].isalnum():
                r -= 1
        
        return True
            
            

            


        