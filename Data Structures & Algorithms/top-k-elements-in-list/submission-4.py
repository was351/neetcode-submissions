class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        res=[]
        bucket=[[]for _ in range(len(nums)+1)]
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for val,count in freq.items():
            bucket[count].append(val)
        count=0
        idx=len(nums)
        while idx>-1:
            if bucket[idx]:
                count+=len(bucket[idx])
                res.extend(bucket[idx])
                if count>=k:
                    break
            idx-=1
        return res


        
        