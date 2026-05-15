class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        res=[]
        buckets=[[]for _ in range (len(nums)+1)]
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for num,val in freq.items():
            buckets[val].append(num)
        i=len(nums)
        count=0
        while i>0:
            if count<k:
                    res.extend(buckets[i])
            if buckets[i]:
                    count+=len(buckets[i])
            i-=1
        return res
