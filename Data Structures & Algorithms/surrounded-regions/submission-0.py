class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visit=set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i==0 or i==len(board)-1 or j==len(board[0])-1 or j==0 and board[i][j]=='O':
                    self.dfs(i,j,visit,board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i,j) not in visit:
                    board[i][j]='X'
        return 

    def dfs(self,i,j,visit,board):
        if i<0 or j<0 or i>=len(board) or j>=len(board[0]):
            return
        if (i,j) in visit:
            return 
        if board[i][j]=='X':
            return
        visit.add((i,j))
        self.dfs(i+1,j,visit,board)
        self.dfs(i-1,j,visit,board)
        self.dfs(i,j+1,visit,board)
        self.dfs(i,j-1,visit,board)
        return 
        
                    
