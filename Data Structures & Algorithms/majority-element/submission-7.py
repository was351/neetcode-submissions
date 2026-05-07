class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        most=(0,0)
        for n in nums:
            count[n]=count.get(n,0)+1
            if count[n]>most[0]:
                most=(count[n],n)
        return most[1]
                  
