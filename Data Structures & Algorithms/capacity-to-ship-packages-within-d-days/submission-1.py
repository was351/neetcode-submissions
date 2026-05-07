class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        total=sum(weights)
        r=total
        while l<r:
            mid= (l + r )// 2 
            total=0
            required=1
            for cargo in weights:
                total+=cargo
                if total>mid:
                    required+=1
                    total=cargo    
            test=total/mid
            if required<=days:
                r=mid
            else:
                l=mid+1
        return r