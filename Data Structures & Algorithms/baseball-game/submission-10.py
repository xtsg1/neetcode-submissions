# rep nov 21

# APPROACH
# many commands have to reach back to the previous score
# even twice
# so we need to not the last scores at least the last 2
# but it can be invalidated too
# so a stack can track all this
# apply each operation]
# integers need a conversion
# the constraints means we dont have to check for edge case where +/C/D applies to an empty list, nice!! i was thinking about this for too long ripppp

# time: O(n) for n operations
# space: O(n) n stack in worst case 

# solved: in 10:50

class Solution:

    def calPoints(self, operations: List[str]) -> int:

        stack = []
        score = 0
        for o in operations:

            if o == "+":
                score = stack[-1] + stack[-2]
                stack.append(score)
            elif o == "D":
                score = stack[-1] * 2
                stack.append(score)
            elif o == "C":
                stack.pop()
            else:
                score = int(o)
                stack.append(score)
        
        sm = sum(stack)
        return sm



        