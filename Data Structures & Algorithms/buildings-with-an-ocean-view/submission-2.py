class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        local=0
        r=len(heights)-1
        res=[]
        while r>=0:
            if heights[r]>local:
                res.append(r)    
            local=max(local,heights[r])
            r-=1
        res.reverse()
        return res
