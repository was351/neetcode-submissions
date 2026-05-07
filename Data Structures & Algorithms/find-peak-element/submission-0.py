class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l=0 
        r=len(nums)-1
        peak=0
        while l < r:
            if nums[l]>=nums[r]:
                r-=1
                peak=l
            else:
                l+=1
                peak=r
        return peak
