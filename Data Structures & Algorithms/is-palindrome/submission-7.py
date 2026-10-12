class Solution:
    def isPalindrome(self, s: str) -> bool:

        tidy = ""
        for char in s:
            if char.isalnum():
                tidy += char.lower()

        i = 0
        j = len(tidy) - 1
        while i < j:
            if tidy[i] != tidy[j]:
                return False
            i += 1
            j -= 1
        
        return True




# r a c e c a r
#   i
#           j