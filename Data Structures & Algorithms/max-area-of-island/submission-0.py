class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area=0
        visit=set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    continue
                elif (i,j) in visit:
                    continue
                else:
                    count=self.dfs(i,j,grid,visit)
                    if count>max_area:
                        max_area=count

        return max_area

    def dfs(self,i,j,grid,visit):
        if i<0 or j<0 or j>=len(grid[0]) or i>=len(grid):
            return 0
        elif (i,j) in visit:
            return 0
        elif grid[i][j]==0:
            return 0
        visit.add((i,j))
        left=self.dfs(i-1,j,grid,visit)
        right=self.dfs(i+1,j,grid,visit)
        up=self.dfs(i,j+1,grid,visit)
        down=self.dfs(i,j-1,grid,visit)
        res=1+left+right+up+down
        return res 
            
        