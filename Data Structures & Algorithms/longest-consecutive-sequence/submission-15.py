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
                cur=0
                for i in range(len(nums)):
                    if vals+i in val:
                        cur+=1
                    else :
                        break
                count=max(count,cur)
        return count 

