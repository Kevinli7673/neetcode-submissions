"""
Meaning: find the shortest substring in s that contains all values in t
Edge case: check if s >= t
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def helper(smap, tmap):
            keycount = 0
            res = 0
            for k in smap:
                if smap[k] >= tmap[k]:
                    res += 1
                keycount += 1
            return keycount == res
                    

        l = 0
        tmap = Counter(t)
        smap = {}
        res = (-1, -1)

        for c in t:
            smap[c] = 0

        for r in range(len(s)):
            if s[r] in smap:
                smap[s[r]] += 1
            while helper(smap, tmap):
                if res == (-1, -1):
                    res = (l, r)
                elif (r-l + 1) < (res[1] - res[0] + 1):
                    res = (l, r)
                if s[l] in smap:
                    smap[s[l]] -= 1
                l += 1

        return s[res[0]:res[1]+1]