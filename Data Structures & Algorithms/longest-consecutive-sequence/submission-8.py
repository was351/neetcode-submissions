class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        if not nums:
            return 0
        longest=1
        while i<len(nums):
            j=i
            
            while j<len(nums)-1:

                if abs(nums[j+1])== (abs(nums[j]+1)):
                    j+=1
                else:
                    break
                if j >longest: 
                        longest=j+1
            i=i+j+1
        return longest

