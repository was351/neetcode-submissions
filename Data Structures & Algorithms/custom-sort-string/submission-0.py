class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq={}
        res=[]
        for l in s:
            freq[l]=freq.get(l,0)+1
        for i in range(len(order)):
            if order[i] in freq:
                for l in range(freq[order[i]]):
                    res.append(order[i])
                del freq[order[i]]
        for key,val in freq.items():
            for i in range(val):
                res.append(key)
        
        return "".join(res)


