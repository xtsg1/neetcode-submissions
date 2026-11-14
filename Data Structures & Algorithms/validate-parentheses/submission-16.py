# rep nov 14

# QUESTION
# valid brackets
# every open bracket closed by same type
# closing order is correct
# every bracket IS closed

# APPROACH
# to track opened bracketse use a stack
# the order of stack tells you which brackets is valid to close
# the existence of any elements left tells you whether everything has been closed
# for bracket validity need a map that maps the open to closed brackets
# couple checks
# cannot close something thats never been opened
# closed brackets must match last opened item in the stack
# properly closed brackets in order gets "ignored", opened brackets get popped from the stack

# TIME: all elements so O(n)
# SPACE: hashmap is O(1), but stack in worst case is O(n) so O(n)


class Solution:

    def isValid(self, s: str) -> bool:

        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        opened = []

        for b in s:

            if b in pairs:

                if not opened: #cant close something thats never opened
                    return False 

                last = opened[-1]
                if pairs[b] != last: # invalid closure
                    return False
                elif pairs[b] == last:
                    opened.pop() # pop off the validly closed bracket
            
            elif b not in pairs:
                opened.append(b)
        
        if opened: #leftovers!
            return False

        return True

#( 

            

        