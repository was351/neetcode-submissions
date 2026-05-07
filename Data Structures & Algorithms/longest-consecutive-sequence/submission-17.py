class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        val=set(nums)
        candidates=[]
        count=0
        if len(nums)==0:
            return count
        for num in nums:
            if num-1 not in val :
                candidates.append(num)
        for vals in candidates:
            cur=1
            check=vals+1
            while check in val:
                check+=1
                cur+=1
           
              
            count=max(count,cur)
        return count 

