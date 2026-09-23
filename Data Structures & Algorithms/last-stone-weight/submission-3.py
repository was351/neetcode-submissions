import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for stone in stones:
            heapq.heappush(heap,-stone)
        while heap:
            print(heap)
            if len(heap)==1:
                return heap[0]*-1
            stone1=heapq.heappop(heap)
            stone2=heapq.heappop(heap)
            if stone1<stone2:
                remain=stone1-stone2
                heapq.heappush(heap,remain)
            print(heap)
            
        return 0
        