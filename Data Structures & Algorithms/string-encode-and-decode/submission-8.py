class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encoding = ""
        for s in strs:
            length = len(s)
            encoding = encoding + str(len(s)) + "#" + s
        return encoding
            

    def decode(self, s: str) -> List[str]:
        
        output = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = start + length
            word = s[start:end]
            output.append(word)
            i = end
        
        return output

                


        