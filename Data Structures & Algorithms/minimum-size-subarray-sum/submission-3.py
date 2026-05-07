class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        r=0
        length=float('inf')
        total=0
        while(r<len(nums)):
            total+=nums[r]
            while total>=target:
                length=min(length,r-l+1)
                total-=nums[l]
                l+=1
            r+=1
            
        if length==float('inf'):
            return 0
        else:
            return length
