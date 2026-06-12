class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit=set()
        check=0
        for i in range (len(grid)):
            for j in range (len(grid[0])):
                if grid[i][j]==1:
                    check=max(self.dfs(i,j,visit,grid),check)
        return check 
    
    def dfs(self,i,j,visit,grid):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
            return 0
        if ((i,j) in visit):
            return 0
        if grid[i][j]==0:
            return 0
        visit.add((i,j))
        right=self.dfs(i+1,j,visit,grid)
        left=self.dfs(i-1,j,visit,grid)
        up=self.dfs(i,j+1,visit,grid)
        down=self.dfs(i,j-1,visit,grid)
        return 1+right+left+up+down
