class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        r=sum(weights)
        l=max(weights)
        while l<r:
            mid=l+(r-l)//2
            total=0
            required=1
            for cargo in weights:
                total+=(cargo)
                if total>mid:
                    required+=1
                    total=cargo
            if required<=days:
                r=mid
            else:
                l=mid+1
        
        return r
                
