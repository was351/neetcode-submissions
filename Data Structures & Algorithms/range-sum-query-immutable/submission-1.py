class NumArray:

    def __init__(self, nums: List[int]):
        sum=0
        self.prefix=[0]

        for i in range(len(nums)):
            sum+=nums[i]
            self.prefix.append(sum)
            

            
            
        

    def sumRange(self, left: int, right: int) -> int:
    
            return (self.prefix[right+1]-self.prefix[left])

