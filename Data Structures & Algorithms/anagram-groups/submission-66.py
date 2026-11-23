# GREEN 2026-11-23 | first try, no hints, 5:36 | review ~Dec 14
# rep nov 23



# APPROACH
# start by sorting the anagrams
# this gets us a key that will be the same as long as another word belongs to thsi anagram class
# with that key populate a dictionary
# lets try it with a defaultdict this time, inits empty dicts which is nice
# then for each grouped list, populate a new list with the values only (the grouped anagrams)

# time: sorting gives us O(nlogn)
# space: we require an extra dict that grows with the size of n so O(n)

# solved: 5:36

from collections import defaultdict

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list)

        for s in strs:
            k = "".join(sorted(s))
            groups[k].append(s)
        
        res = []
        for g in groups.values():
            res.append(g)
        
        return res

        


        