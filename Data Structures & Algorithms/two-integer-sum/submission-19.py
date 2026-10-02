class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i, num in enumerate(nums):
            seen[num]=i
    
        for i, num in enumerate(nums):
            required_value=target-num
            if required_value in seen:
                j=seen[required_value]
                if j<i:
                    return [j,i] 
                elif i !=j:
                    return[i,j]


            
                

            

                
