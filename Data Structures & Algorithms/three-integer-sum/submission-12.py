class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]

        
        nums.sort()
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                cur=nums[l]+nums[r]+nums[i]
                
                print(i,l,r,cur)
                if cur == 0:
                    
                    res.append([nums[i],nums[l],nums[r]])  
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1]:
                        l-=1
                   
                if cur>0:
                    r-=1
                else:
                    l+=1
        return list(res)




            