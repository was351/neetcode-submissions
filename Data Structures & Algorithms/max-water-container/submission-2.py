class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        max_water=0
        while l<r:
            min_val=min(heights[l],heights[r])
            cur=min_val*(r-l)
            max_water=max(max_water,cur)
            if(min_val==heights[l]):
                l+=1
            else:
                r-=1
        return max_water

        