class Solution:
    def isValid(self, s: str) -> bool:
        opened = []

        for c in s:
            if c in [")", "}", "]"] and not opened:
                return False
            elif c in ["(", "{", "["]:
                opened.append(c)
            elif c == ")":
                if opened[-1] == "(":
                    opened.pop()
                else:
                    return False
            elif c == "}":
                if opened[-1] == "{":
                    opened.pop()
                else:
                    return False
            elif c == "]":
                if opened[-1] == "[":
                    opened.pop()
                else:
                    return False
        
        if not opened:
            return True
        return False




# () {} []