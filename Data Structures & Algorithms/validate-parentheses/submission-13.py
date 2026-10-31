# rep oct 31

# QUESTION
# all brackets closed
# closed order matters, inner brackets must be closed before outer
# cant close something that hasn't been opened
# must close a matching bracket


# APPROACH
# start with a hashmap of each bracket and it's "partner"
# opening brackets get added to a stack
# closing brackets need checks
    # is there a corresponding open bracket?
    # is it immediately adjacent (closable)
    # a succesfully closure means we can pop the last element too (the previous opened bracket)
# at the end the stack being empty means every bracket that was opened is also closed
# if all are true then the string is valid
# time: O(n) every element of s seen once
# space: the stack in the worst case can be as large as half of s so O(n) too

# WALKTHROUGH
# ( [ { } ] )

# opened  = ( [ { <-- last item

class Solution:
    
    def isValid(self, s: str) -> bool:

        pairs = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        opened = []

        for c in s:
            
            if c in pairs:

                if not opened:  # closing something thats never been opened
                    return False
                
                if pairs[c] != opened[-1]: # closing wrong bracket
                    return False

                if pairs[c] == opened[-1]:  # valid closure
                    opened.pop()

            else:
                opened.append(c)
        
        return not opened
                
                
                



