import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for stone in stones:
            heapq.heappush(heap,-stone)
        while heap:
            if len(heap)==1:
                return -heap[0]
            s1=heapq.heappop(heap)
            s2=heapq.heappop(heap)
            if abs(s2-s1)>0:
                heapq.heappush(heap,-abs(s2-s1))

        return 0
