class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic1={}
        diff=0
        length=len(nums)
        for i in range(length):
         diff=target-nums[i]
         if (diff in dic1): 
            return [dic1[diff],i]
         dic1[nums[i]]=i
    
