class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        empty=len(nums1)-1
        largest_num1=len(nums1)-len(nums2)-1
        largest_num2=len(nums2)-1
        while empty > largest_num1:
            if largest_num1 == -1 or nums2[largest_num2]>nums1[largest_num1]:
                nums1[empty]=nums2[largest_num2]
                largest_num2-=1
                empty-=1
            else:
                nums1[empty]=nums1[largest_num1]
                largest_num1-=1
                empty-=1
            

            
        