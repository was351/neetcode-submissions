class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=1
        while j<len(nums):
            if nums[i]==nums[j]:
                del nums[i]
                j-=1
                i-=1
            i+=1
            j+=1
        return(len(nums))



