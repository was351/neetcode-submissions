class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem={}
        for idx,num in enumerate(nums):
            if target-num in rem:
                return [rem[target-num],idx]
            rem[num]=idx
        