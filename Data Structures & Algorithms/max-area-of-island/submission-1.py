class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit=set()
        count=0
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) in visit:
                    continue
                elif grid[i][j]==0:
                    continue
                count=self.dfs(i,j,grid,visit)
                res=max(res,count)
        return res
    def dfs(self,i,j,grid,visit):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
            return 0
        elif (i,j) in visit:
            return 0
        elif grid[i][j]==0:
            return 0
        visit.add((i,j))
        right=self.dfs(i+1,j,grid,visit)
        left=self.dfs(i-1,j,grid,visit)
        up= self.dfs(i,j+1,grid,visit)
        down= self.dfs(i,j-1,grid,visit)

        return 1+right+up+down+left
            
