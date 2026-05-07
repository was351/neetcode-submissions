class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        count=0
        i=0
        inc=True
        dec=True
        while i<len(nums)-1:
            if nums[i]>nums[i+1]:
                inc=False
        
            if nums[i]<nums[i+1]:
                dec=False
            i+=1
        return inc or dec


