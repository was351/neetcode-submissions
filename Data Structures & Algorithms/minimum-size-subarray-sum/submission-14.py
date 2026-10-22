class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #since adding numbers is always positive, remove values will always lower the running sum

        l=0
        curSum=0
        length=len(nums)+1
        for r in range(len(nums)):
            curSum+=nums[r]
            while curSum>=target:
                length=min(length,r-l+1)
                curSum-=nums[l]
                l+=1
        return length if length <len(nums)+1 else 0


