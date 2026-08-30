class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        i = lower
        res = []
        val=set(nums)
        while i <= upper:
            if i not in val:
                l = i

                while i <= upper and i not in nums:
                    i += 1

                res.append([l, i - 1])
            
            else: i += 1

        return res