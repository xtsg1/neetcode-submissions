class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        opened = []

        for c in s:
            if c in pairs:
                if opened and opened[-1] == pairs[c]: # valid closure of last item in stack
                    opened.pop()
                else:
                    return False
            else:
                opened.append(c)

        if not opened:
            return True
        return False
            

        