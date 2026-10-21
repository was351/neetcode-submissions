class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen=set()
        count=0
        for i in range(len(grid)):
            for j in range (len(grid[0])):
                if grid[i][j]=='1' and (i,j) not in seen:
                    count+=1
                    self.dfs(i,j,seen,grid)
                
        return count 
    
    def dfs(self,i,j,seen,grid):
        if i<0 or j<0 or i>=len(grid)or j>=len(grid[0]):
            return 
        if (i,j) in seen:
            return 
        if grid[i][j]=='0':
            return
        seen.add((i,j))
        self.dfs(i+1,j,seen,grid)
        self.dfs(i-1,j,seen,grid)
        self.dfs(i,j+1,seen,grid)
        self.dfs(i,j-1,seen,grid)
        return

        