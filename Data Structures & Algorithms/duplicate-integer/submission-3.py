class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_dict: Dict[str, int] = {}
        for key in nums:
                if key in dup_dict:
                    return True
                else:
                    dup_dict[key]= 1
        
        return False
        