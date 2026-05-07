class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count={}
        cur=[]
        res=[]
        for num in nums:
            count[num]=count.get(num,0)+1
        print(count)
        def perm():
            if len(cur)==len(nums):
                res.append(cur.copy())
            for num in count :
                if count[num]==0:
                    continue
                cur.append(num)
                count[num]-=1
                print(count)
                perm()
                cur.pop()
                count[num]+=1
        perm()
        return res
