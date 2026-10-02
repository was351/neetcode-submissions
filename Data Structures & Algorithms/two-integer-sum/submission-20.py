class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i, num in enumerate(nums):
            required=target-num
            if required in seen:
                j=seen[required]
                if j<i:
                    return [j,i]
                return [i,j]
            seen[num]=i

    
     


            
                

            

                
