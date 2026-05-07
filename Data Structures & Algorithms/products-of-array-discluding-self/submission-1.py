class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        def prefix(index, number: list[int]):
            pre_product = 1
            i = 0
            while i < index:
                pre_product *= number[i]
                i += 1
            return pre_product
        
        def postfix(index, number: list[int]):
            post_product = 1
            i = len(number) - 1
            while i > index:
                post_product *= number[i]
                i -= 1
            return post_product

        result = []
        for index, val in enumerate(nums):
            prod = 1
            if index > 0:
                prod *= prefix(index, nums)
            if index < len(nums) - 1:
                prod *= postfix(index, nums)
            result.append(prod)

        return result
           
                