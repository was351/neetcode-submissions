class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic1={}
        length=len(nums)
        for i in range(length):
         diference=target-nums[i]
         if (differnece in dic1):
            return [dict[difference],i]
         dic1[diference]=i
    
