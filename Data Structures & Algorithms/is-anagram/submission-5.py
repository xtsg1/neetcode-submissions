class Solution:
    
    def get_freq_map(self, word: str) -> dict:
        seen = {}
        for letter in word:
            if letter not in seen:
                seen[letter] = 1
            elif letter in seen:
                seen[letter] += 1
        
        return seen

    def isAnagram(self, s: str, t: str) -> bool:
        
        s_map = self.get_freq_map(word=s)
        t_map = self.get_freq_map(word=t)
        is_anagram = s_map == t_map
        return is_anagram

