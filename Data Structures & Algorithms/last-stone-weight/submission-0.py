import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for val in stones:
            heapq.heappush(heap,-val)  
        
        while len(heap)>1:
            num1=heapq.heappop(heap)
            num2=heapq.heappop(heap)
            ans=num1-num2
            heapq.heappush(heap,ans)
        return heap[0]*-1



    