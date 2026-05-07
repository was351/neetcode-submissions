class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen=set()
        res=[]
        count=0
        for i in range (len (grid)):
            for j in range (len(grid[0])):
                if grid[i][j] in seen:
                    res.append(grid[i][j]) 
                else:
                    seen.add(grid[i][j])
                count+=1
        
        for i in range (1,count+1):
            if i not in seen:
                res.append(i)
                return res
                
                
                    
