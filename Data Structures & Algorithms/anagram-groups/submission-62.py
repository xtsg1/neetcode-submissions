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


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}

        for word in strs:

            sortkey = "".join(sorted(word))
            if not anagrams.get(sortkey):
                anagrams[sortkey] = [word]
            else:
                anagrams[sortkey].append(word)
            
            
        
        
        res = []
        for sublist in anagrams.values():
            res.append(sublist)
    
        return res 
        
            


        

        