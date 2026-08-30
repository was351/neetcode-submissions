class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        longest=1
        while i<len(nums):
            j=i
            
            while j<len(nums)-1:

                if nums[j+1]== (nums[j]+1):
                    j+=1
                else:
                    break
                if j >longest: 
                        longest=j
            i=i+j+1
        return longest

