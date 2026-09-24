import heapq,math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        res=[]
        for x,y in points:
            distance=-(x**2 + y**2)
            heapq.heappush(heap,(distance,[x,y]))
            while len(heap)>k:
                heapq.heappop(heap)
                   
        for i in range(len(heap)):
            res.append(heap[i][1])
        return res