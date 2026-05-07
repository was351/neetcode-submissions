class Solution:
    def countElements(self, arr: List[int]) -> int:
       val=set(arr) 
       count=0
       for num in arr:
            if num+1 in val:
                count+=1
       return count