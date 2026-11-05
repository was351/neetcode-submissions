class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)== 0:
            return 0;
        slow = 0 
        fast = 1;
        while fast < len(nums):
            if nums[fast] == nums[slow]:
                fast +=1
            else:
                 slow +=1
                 nums[slow] = nums[fast]
        return slow+1


    
    
        
                


        



