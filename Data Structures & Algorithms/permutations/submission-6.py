class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        cur=[]
        res=[]
        cur_set=set()
        self.rec(nums,cur,res,cur_set)
        return res
    
    def rec(self,nums,cur,res,cur_set):
        if len(cur)==len(nums):
            res.append(cur.copy())
            return 
        for i in range(len(nums)):
            if nums[i] not in cur_set:
                cur.append(nums[i])
                cur_set.add(nums[i])
                self.rec(nums,cur,res,cur_set)
                cur_set.remove(cur[-1])
                cur.pop()
               
        return

        
        