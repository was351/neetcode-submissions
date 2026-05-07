import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        heap=[]
        res=[]
        for num in nums:
            count[num]=count.get(num,0)+1
        for key,v in count.items():
            heapq.heappush(heap,(v,key))
            while len(heap)>k:
                heapq.heappop(heap)
        for val in heap:
            a,b=val
            res.append(b)
        return res



