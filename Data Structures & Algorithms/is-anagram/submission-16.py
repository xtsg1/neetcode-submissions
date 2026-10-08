class Solution:

    def get_freq(self, s: str) -> dict[str, int]:
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        return freq


    def isAnagram(self, s: str, t: str) -> bool:
        return self.get_freq(s) == self.get_freq(t)


        



