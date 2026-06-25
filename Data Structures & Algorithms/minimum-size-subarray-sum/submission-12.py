class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length=float('inf')
        total=0
        l=0
        for r in range(len(nums)):
            total+=nums[r]
            while total>=target and l<=r:
                length=min((r-l+1),length)
                total-=nums[l]
                l+=1
                
               
           
       
        return length if length!=float('inf') else 0
