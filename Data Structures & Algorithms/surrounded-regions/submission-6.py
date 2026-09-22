class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visit=set()
        grid=board
        for i in range (len(grid)):
            for j in range(len(grid[0])):
                if i==0 or j==0 or i==len(grid)-1 or j==len(grid[0])-1 and grid[i][j]=='O':
                        self.dfs(i,j,grid,visit)

        
        for i in range (len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visit:
                    grid[i][j]="X"
        return 
    def dfs(self,i,j,grid,visit):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
            return 
        if (i,j) in visit:
            return
        if grid[i][j]=="X":
            return 
        visit.add((i,j))
        self.dfs(i+1,j,grid,visit)
        self.dfs(i-1,j,grid,visit)
        self.dfs(i,j+1,grid,visit)
        self.dfs(i,j-1,grid,visit)
        return 
