import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heap=[]
        for stick in sticks:
            heapq.heappush(heap,stick)
        cost=0
        while len(heap)>1:
            temp1=heapq.heappop(heap)
            temp2=heapq.heappop(heap)
            comb=temp1+temp2
            cost+=comb
            heapq.heappush(heap,comb)
        return cost

        