class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        if not nums:
            return 0
        longest=1
        while i < len(nums):
            j = i

            while j < len(nums) - 1:
                if nums[j + 1] == nums[j] + 1:
                    j += 1
                elif nums[j + 1] == nums[j]:
                    j += 1   # skip duplicates
                else:
                    break

            longest = max(longest, j - i )
            i = j+1
        return longest

