class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string1 = defaultdict(int)
        string2 = defaultdict(int)

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            string1[s[i]] += 1
            string2[t[i]] += 1
        
        if string1 == string2:
            return True
        else:
            return False