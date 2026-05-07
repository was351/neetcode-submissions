# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.split(pairs)
    
    def split(self,arr):
        if len(arr)<2:
            return arr
        mid=len(arr)//2
        left=self.split(arr[:mid])
        right=self.split(arr[mid:])
        return self.merge(left,right)

    def merge(self,left,right):
        arr=[]
        l=0
        r=0
        while l<len(left) or r<len(right):
            if l>=len(left):
                arr.append(right[r])
                r+=1
            elif r>=len(right):
                arr.append(left[l])
                l+=1
            elif right[r].key >= left[l].key:
                arr.append(left[l])
                l+=1
            else:
                arr.append(right[r])
                r+=1
        return arr