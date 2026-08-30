class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted(nums)
        print(nums)
        res=[]
        for i in range (len(nums)):
            l=i+1
            r=nums-1
            while l<r:
                if  nums[i]+nums[r]+nums[r]==0:
                    res.append[nums[i],nums[l],nums[r]]
                    l+=1
                    while nums[i]+nums[r]+nums[l]==0:
                        res.append[nums[i],nums[l],nums[r]]
                        l+=1
                elif nums[i]+nums[l]+nums[r]<0:
                    l+=1
                else:
                    r+=1
            return res
                    
            

                    
