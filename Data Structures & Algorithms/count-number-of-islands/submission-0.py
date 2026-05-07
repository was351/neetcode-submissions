class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        visit=set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i,j) in visit:
                    continue
                if grid[i][j]=='1':
                    count+=1
                    self.dfs(i,j,grid,visit)
            
                
        return count
    def dfs(self,i,j,grid,visit):

        if i>=len(grid)or j>=len(grid[i])or j<0 or i<0:
            return 

        if (i,j) in visit:
            return
        if grid[i][j]=='0':
            return 
        visit.add((i,j))
        self.dfs(i+1,j,grid,visit)
        self.dfs(i-1,j,grid,visit)
        self.dfs(i,j+1,grid,visit)
        self.dfs(i,j-1,grid,visit)

        