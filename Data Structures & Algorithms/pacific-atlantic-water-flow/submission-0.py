class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res=[]
        pacific=set()
        atlantic=set()
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if j==0 or i==0:
                    self.dfs(-1,i,j,heights,pacific)
                if j==len(heights[0])-1 or i==len(heights)-1:
                    self.dfs(-1,i,j,heights,atlantic)
                  
        print(atlantic)
        print(pacific)
        for item in pacific:
            if item in atlantic:
                print(item)
                a,b=item
                res.append([a,b])
        return res


    
    def dfs(self,prev,i,j,grid,visit):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]): 
            return
        if (i,j) in visit:
            return
        if grid[i][j]<prev:
            return
        
        visit.add((i,j))
        self.dfs(grid[i][j],i+1,j,grid,visit)
        self.dfs(grid[i][j],i-1,j,grid,visit)
        self.dfs(grid[i][j],i,j+1,grid,visit)
        self.dfs(grid[i][j],i,j-1,grid,visit)

        


        
