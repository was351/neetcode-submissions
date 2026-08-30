class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length=float('inf')
        total=0
        l=0
        for r in range(len(nums)):
            total+=nums[r]
            while total>=target:
                length=min((r-l+1),length)
                l+=1
                total-=nums[l]
               
           
       
        return length if length!=float('inf') else 0
