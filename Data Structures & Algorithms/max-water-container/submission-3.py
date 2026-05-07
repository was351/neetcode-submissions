class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        max_w=min(heights[l],heights[r])*(r-l)
        while l<r:
            print(l,r)
            area=min(heights[l],heights[r])*(r-l)
            max_w=max(area,max_w)
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return max_w