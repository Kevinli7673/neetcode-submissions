"""
Return the k amount of points that are the cloest to the origin (0,0)
Idea: for every point in the list: we create a tuple (distance, point)
After that we heapify and for k amt we pop and add it to res
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        points = [((math.sqrt((p[0] - 0)**2 + (p[1] - 0)**2)), p) for p in points]
        
        heapq.heapify(points)
        print(points)

        for i in range(k):
            x = heapq.heappop(points)
            res.append(x[1])

        return res