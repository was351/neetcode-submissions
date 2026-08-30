class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        seen=set()
        
        nums.sort()
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<=r:
                cur=nums[l]+nums[r]+nums[i]
                if cur == 0:
                    if (nums[i],nums[l],nums[r]) not in seen:
                        res.append([nums[i],nums[l],nums[r]])
                        seen.add((nums[i],nums[l],nums[r]))
                    l+=1
                if cur>0:
                    r-=1
                else:
                    l+=1
        return list(res)




            