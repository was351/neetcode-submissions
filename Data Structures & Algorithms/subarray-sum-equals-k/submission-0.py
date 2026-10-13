from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre=defaultdict(int)
        count=0
        running=0
        pre[0]=1
        for i in range(len(nums)):
            print(running)
            running+=nums[i]
            count+=pre[running-k]
            pre[running]+=1
        
        return count
            


            
        