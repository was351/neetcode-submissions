class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index={}
        for i in range(len(nums)):
            index[nums[i]]=i
        for j in range(len(nums)): 
            remain=target-nums[j]
            if remain in index and index[remain]!=j:
                return[j,index[remain]]
        return []

      