class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        fs = []
        ss = []
        sss =[]

        for letter in s:
            fs.append(letter)
        
        for letter in t:
            ss.append(letter)
            sss.append(letter)

        for i,n in enumerate(fs):
            for x,y in enumerate(ss):
                if(n == y):
                    ss.pop(x)
                    break
        
        if not ss and len(sss) == len(fs):
            return True
        else:
            return False
