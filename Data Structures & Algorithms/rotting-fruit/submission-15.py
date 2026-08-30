class Solution:
    from collections import deque 
    def orangesRotting(self, grid: List[List[int]]) -> int:
        counter=0
        queue=deque()
        visit=set ()
        time=0
        for i in range (len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    counter+=1
                elif grid[i][j]==2:
                    queue.append((i,j))
                    visit.add((i, j))
        if counter==0:
            return 0
        while queue and counter > 0:
            time += 1
            for k in range(len(queue)):
                i,j=queue.popleft()

                directions=[[0,1],[1,0],[-1,0],[0,-1]]
                ni, nj = i+dx, j+dy
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == 1 and (ni, nj) not in visit:
                    visit.add((ni, nj))
                    counter -= 1
                    queue.append((ni, nj))
                time+=1

