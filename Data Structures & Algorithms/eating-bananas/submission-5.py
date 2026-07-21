"""
Idea:
Brute force: 
problem is at least O(n)

"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = float("inf")

        if len(piles) < 2:
            return math.ceil(piles[0]/h)

        while l<=r:
            m = (l+r) // 2
            hours = 0

            for i in piles:
                hours += math.ceil(i/m)

            if hours <= h:
                r = m-1
                res = min(m, res)
            elif hours > h:
                l = m+1
        return res