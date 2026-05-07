import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        res=[]
        for point in points:
            distance=(point[0])**2+(point[1])**2
            tup=(-distance,point)
            heapq.heappush(heap,tup)
            while len(heap)>k:
                heapq.heappop(heap)
        
        while heap:
            dis,arr=heapq.heappop(heap)
            res.append(arr)
        return res
