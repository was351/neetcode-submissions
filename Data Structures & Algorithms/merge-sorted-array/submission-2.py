class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1=m-1
        p2=n-1
        idx=m+n-1
        while idx>=0 and p1>=0 and p2>=0:
            print(f"idx={idx} {p1} n={p2} nums1={nums1}")
            if nums1[p1]>=nums2[p2]:
                nums1[idx]=nums1[p1]
                p1-=1
            else:
                nums1[idx]=nums2[p2]
                p2-=1
            idx-=1
        while idx>=0 and p2>=0:
            print(f"idx={idx} m={m} n={n} nums1={nums1}")
            nums1[idx]=nums2[p2]
            idx-=1
            p2-=1
        return 

           
        
 
