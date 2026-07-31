"""
Brute force: use a for loop and nested for loop for finding every possibility

Better alternative: 
We iterative through once, finding how long each consecutive char is, then we can swap the lower amt of longest string
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        res, maxFreq = 0, 0
        freqMap = defaultdict(int)

        for r in range(len(s)):\

            freqMap[s[r]] += 1
            
            maxFreq = max(maxFreq, freqMap[s[r]])

            if ((r-l) + 1) - maxFreq > k:
                curr = s[l]
                while l < len(s) and s[l] == curr and ((r-l) + 1) - maxFreq > k:
                    freqMap[s[l]] -= 1
                    l += 1
            

            res = max(res, r-l+1)

        return res