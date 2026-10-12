class Solution:

    map = {
        ")": "(",
        "}": "{",
        "]": "[",
    }

    def isValid(self, s: str) -> bool:
        
        opened = []

        for c in s:

            if c in self.map.values():
                opened.append(c)

            if c in self.map.keys():
                if not opened:
                    return False
                if self.map[c] != opened[-1]: #unmatching complement e.g. {), [}
                    return False
                opened.pop()

        return not opened




# () {} []