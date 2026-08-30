class Solution:
    from collections import deque 
    def orangesRotting(self, grid: List[List[int]]) -> int:
        counter=0
        queue=deque()
        visit=set ()
        time=-1
        for i in range (len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    counter+=1
                elif grid[i][j]==2:
                    queue.append((i,j))

        while queue:
            print(len(queue), time)
            for k in range(len(queue)):
                i,j=queue.popleft()
                if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
                    continue 
                if (i,j) in visit:
                    continue
                visit.add((i,j))
                if grid[i][j] == 0:
                    continue
                
                print((i, j))

                if grid[i][j] == 1:
                    counter-=1

                directions=[[0,1],[1,0],[-1,0],[0,-1]]
                for dx,dy in directions:
                    if i+dx>=0 and  j+dy>=0 and i+dx<len(grid) and j+dy<len(grid[0]):
                       queue.append((i+dx,j+dy))
            if queue:
                time+=1
        return time if counter==0 else -1
