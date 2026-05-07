class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket=[[]for _ in range(len(nums) + 1)]
        counter={}
        result=[]
        i=len(nums)
        for val in nums:
            if val in counter:
                counter[val]+=1
            else: 
                counter[val]=1
        for key,value in counter.items():
            bucket[value].append(key)

        while i > 0:
           if bucket[i]:
                result.extend(bucket[i])
                if len(result) == k:
                   return result
           i-=1 
        return[]  
            

            


        

        
        
            

