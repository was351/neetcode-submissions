class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length=float('inf')
        total=0
        l=0
        for r in range(len(nums)):
            while total>=target:
                if total>target:
                    length=min((r-l),length)
                total-=nums[l]
                l+=1
            total+=nums[r]
       
        return length if length!=float('inf') else 0
