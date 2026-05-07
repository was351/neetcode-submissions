# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.split(pairs)
        
    def split(self, arr):
        mid=len(arr)//2
        if len(arr)<2:
            return arr
        left=self.split(arr[:mid])
        right=self.split(arr[mid:])
        return self.merge(left,right)

    def merge(self, left,right):
        arr=[]
        l,r=0,0
        while l<len(left) and r<len(right):
            if left[l].key <= right[r].key:
                arr.append(left[l])
                l+=1
            else :
                arr.append(right[r])
                r+=1
        while l<len(left):
            arr.append(left[l])
            l += 1
        while r < len(right):
            arr.append(right[r])
            r += 1
        return arr

