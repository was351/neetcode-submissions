class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        temp=min(heights[i],heights[j])
        max_area=(j-i)*temp
        while i<j:
            temp=min(heights[i],heights[j])
            if ((j-i)*temp)>max_area:
                max_area=(j-i)*temp

            if heights[i]>heights[j]:
                j-=1
            else:
                i+=1
        return max_area
        
    




        


