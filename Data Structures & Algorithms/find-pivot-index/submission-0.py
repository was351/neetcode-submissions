class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix=[0]
        sum=0
        total=0
        postfix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            sum+=nums[i]
            prefix.append(sum)
        for i in range(len(nums)-1,-1,-1):
            total+=nums[i]
            postfix[i]=total
        for i in range(len(nums)):
            if postfix[i+1]==prefix[i]:
                return i
        else:
            return -1

