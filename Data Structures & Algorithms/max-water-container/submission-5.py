class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        maxArea=min(heights[r],heights[l])*(r-l)
 
        while(r>l):
            cur=min(r,l)*(r-l)*(r-l)
       
            maxArea=max(maxArea,cur)
            if heights[l]>=heights[r]:
                r-=1
              
            else:
                l+=1
            
        return maxArea
            