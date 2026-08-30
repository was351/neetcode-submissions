class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic1={}
        differnece=0
        length=len(nums)
        for i in range(length):
         differnece=target-nums[i]
         if (differnece in dic1):
            return [dict[differnece],i]
         dic1[differnece]=i
    
