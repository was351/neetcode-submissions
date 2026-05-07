class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
       
        res=[]
        def recurse (i,cur,total):
         
            print(cur)
            if i>=len(nums) or total>target:
                return
            if total==target:
                res.append(cur.copy())
                return
            
            
            cur.append(nums[i])
            recurse(i,cur,total+nums[i])
            cur.pop()
            recurse(i+1,cur,total)


        recurse(0,[],0)
        return res
