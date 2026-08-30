class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        r=1
        length=float('inf')
        total=0
        while(r<len(nums)):
            for i in range(l,r,1):
                total+=nums[i]
            if total>10:
                length=min(length,r-l)
                l+=1
            r+=1
            
        if length==float('inf'):
            return 0
        else:
            return length
