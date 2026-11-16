# YELLOW 2026-11-16 | own plan + code in ~5-10 min; ~30 min total: needed help seeing that .get() returns the value and an empty list is falsy (if-branch never stored the first word) | complexity: O(n*k log k) time, O(n*k) space | redo ~Nov 20
# rep nov 16

# QUESTION
# list of lists of strings
# same characters different order
# grouped together by anagrams of one another
# return any order

# APPROACH
# if you sort each string - anagrams become equivalent. Sorting is O(nlogn)
# you can use the sorted string as a key of a hashmap to group by
# append anagrams of the sorted key to the values
# return the list of lists

# Time: sort worse case is O(nlogn)
# space: needs a whole new hashmap grows in proportion with list size is O(n)

# WALKTHROUGH
# word = act
# sortkey = act
# anagrams {act: [act]}
# word = pots
# sortkey = opst
# anagrams {opst: [pots]}
# word = tops
# sortkey = opst
# anagrams {opst: [pots, tops]}
# res = [ [act, cat...], [pots, tops...]]

# solved: ugghh 99% solution in 10ish minutes and lost 15+ minutes over 25 min total fucking aroud with some stupid python shit 


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}

        for word in strs:

            sortkey = "".join(sorted(word))
            if not anagrams.get(sortkey):
                anagrams[sortkey] = [word] # this line fucking killed me god damn it
            else:
                anagrams[sortkey].append(word)
            
            
        
        
        res = []
        for sublist in anagrams.values():
            res.append(sublist)
    
        return res 
        
            


        

        