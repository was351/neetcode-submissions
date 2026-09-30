import math,heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq={}
        heap=[]
        res=[]
        for l in s:
            freq[l]=freq.get(l,0)+1
            if freq[l]>math.ceil(len(s)/2):
                return ""
        for key,value in freq.items():
            heapq.heappush(heap,(-value,key))
        temp=None
        while heap:
            curVal,curKey=heapq.heappop(heap)
            res.append(curKey)
            curVal+=1
            if temp:
                heapq.heappush(heap,(temp[0],temp[1]))
            if curVal<0:
                temp=(curVal,curKey)
            else:
                temp=None
        if temp:
            if temp[1]!=res[-1]:
                res.append(temp[1])
        
        return "".join(res) if len(res)==len(s) else ""



        