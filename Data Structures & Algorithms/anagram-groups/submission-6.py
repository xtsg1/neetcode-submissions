class Solution:
    
    def get_word_map(self, word: str) -> dict:
        
        seen = {}
        for letter in word:
            if letter not in seen:
                seen[letter] = 1
            elif letter in seen:
                seen[letter] += 1
        
        return seen



    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       
        seen = []
        for word in strs:
            word_map = self.get_word_map(word=word)
            
            match = False
            for item in seen:
                item_map = self.get_word_map(item[0])
                if word_map == item_map:
                    item.append(word)
                    match = True
                    break
            if match == False:
                seen.append([word])
            


        return seen    






    