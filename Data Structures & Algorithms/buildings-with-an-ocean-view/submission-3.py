class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack=[]
        i=(len(heights)-1)
        res=[]
        if heights[i]:
            stack.append((heights[i],i))
            i-=1
        while i>=0:
            if heights[i]>stack[-1][0]:
                stack.append((heights[i],i))
            i-=1
        
        for val,idx in stack:
            res.append(idx)
        res.reverse()
        return res