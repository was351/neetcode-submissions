class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        total=n*m
        first=0
        last=total-1
        while first<=last:
            mid=first+(last-first)//2
            row=mid// m
            col=mid% m
            if matrix[row][col]<target:
                last=mid-1
            elif matrix[col][row]>target:
                first=mid+1
            elif matrix[col][row] ==target:
                return true
        return false



        