class Solution:

    def encode(self, strs: List[str]) -> str:
        together = ""
        for string in strs:
            together += "#".join([str(len(string)), string])
        return together


    def decode(self, s: str) -> List[str]:
        length, i, j = 0, 0, 0
        output = []
        while i < len(s):
            j = s.index("#", i)
            length = int(s[i:j])
            i = j + 1
            output.append(s[i:i+length])
            i += length
        return output
