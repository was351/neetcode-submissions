class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:   
        nums.sort()
        res=set()
        ans=[]
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                temp=nums[i]+nums[l]+nums[r]
                if temp==0:
                    res.add((nums[i],nums[l],nums[r]))
                    l+=1
                if temp>0:
                    r-=1
                if temp<0:
                    l+=1
                
        for collection in res:
            ans.append(list(collection))
        return ans
    

