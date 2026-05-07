class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement not in complements:
                complements[num] = idx
            else:
                return [complements[complement], idx]

        return []