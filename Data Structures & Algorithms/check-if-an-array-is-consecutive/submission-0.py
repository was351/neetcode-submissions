class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        dedupe=set(nums)
        return len(nums)==len(dedupe) and (max(nums)-min(nums)+1)==len(nums)