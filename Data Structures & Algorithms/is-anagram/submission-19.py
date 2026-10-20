class Solution:

    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_count = {}
        for c in s:
            s_count[c] = s_count.get(c, 0) + 1
        
            
        t_count = {}
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1
        
        return s_count == t_count

# O(n)
# O(s + t)

# {a: 4, b:2: x: 3}
# {a: 4, b:2: x: 3}


# a n a g r a m
# same chars
# same freq

# in other words a dictionary of counts