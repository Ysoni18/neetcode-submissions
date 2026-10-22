class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in strs:
            peice = str(len(i)) + "#" + i
            result = result + peice
        
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            length_text = ""

            while s[i] != "#":
                length_text += s[i]
                i += 1
            
            length = int(length_text)
            i += 1

            word = s[i:i + length]
            result.append(word)

            i += length
        
        return result