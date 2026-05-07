import heapq 
class MedianFinder:

    def __init__(self):
       self.max_heap=[]
       self.min_heap=[]

    def addNum(self, num: int) -> None:
       
        if self.min_heap and self.min_heap[0]<=num:
            heapq.heappush(self.min_heap,num)
        else:
            heapq.heappush(self.max_heap,-num)
         
        if len(self.min_heap)-len(self.max_heap)>1 and self.min_heap:
            temp=-heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,temp)
        elif len(self.max_heap)-len(self.min_heap) >1 and self.max_heap:
            temp=-heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap,temp)
        

    def findMedian(self) -> float:
        min_l=len(self.min_heap)
        max_l=len(self.max_heap)
        if min_l > max_l :
            return self.min_heap[0]
        elif max_l > min_l:
            return self.max_heap[0]*-1
        else:
            mid=(self.min_heap[0]+self.max_heap[0]*-1)/2.0
            return mid

        