class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        longest=0
        while i<len(nums):
            j=i
            if len(nums)==0:
                return 1
            while j<len(nums)-1:
                if nums[j+1]== (nums[j]+1):
                    j+=1
                    if j >longest: 
                        longest=j
                else:
                    break
            i=i+j+1
        return longest

