"""
Idea: At every step we want the two biggest vals in the heap
Since theres only min heap we can make everything negative
Pop the "Smallest" twice and compare them, append or don't base on the size
keep going until theres one rock left
"""
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-s for s in stones] 
        heapq.heapify(stones)


        while stones and len(stones) != 1:
            print(stones)
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x == y:
                continue
            elif x < y:
                heapq.heappush(stones, -1*((-1*x) - (-1*y)))
        
        if not stones:
            return 0
        return -stones[0]