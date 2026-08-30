class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        highest=0
        for i in range (len(nums)):
            if nums[i] not in count:
                count[nums[i]]=1
            else:
                count[nums[i]]+=1
                if count[nums[i]]>highest:
                    highest=count[nums[i]]
            if highest > (len(nums))//2:
                return count[nums[i]]
      
                
