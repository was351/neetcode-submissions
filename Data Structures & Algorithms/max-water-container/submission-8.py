class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        area=min(heights[l],heights[r])*(r-l)
        while l<r:
            cur=min(heights[l],heights[r])*(r-l)
            print(cur)
            area=max(area,cur)
            if heights[l]>=heights[r]:
                r-=1
            else:
                l+=1
        return area


