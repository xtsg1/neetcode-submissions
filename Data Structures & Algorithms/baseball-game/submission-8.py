# first try nov 7

# APPROACH

# a running list with order
# C pop the list
# D adds last element * 2
# + is last 2 items added
# finally sum the list


# took me 15 min

class Solution:

    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for o in operations:

            try:
                n = int(o)
                stack.append(n)
            except:
                pass

            if o == "+":
                nsum = stack[-1] + stack[-2]
                stack.append(nsum)
            elif o == "D":
                nprod = stack[-1] * 2
                stack.append(nprod)
            elif o == "C":
                stack.pop()
            
        
        tsum = sum(stack)
        return tsum
        