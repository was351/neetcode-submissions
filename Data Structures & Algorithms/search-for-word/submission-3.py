class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visit=set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                 if board[i][j]== word[0]:
                    if self.dfs(i,j,visit,word,board,0):
                        return True
        return False 
    def dfs(self,i,j,visit,word,board,count):
        if i<0 or j<0 or j>=len(board[0]) or i>=len(board):
            return False
        if (i,j) in visit:
            return False
        if board[i][j]!=word[count]:
            return False 
        if count==len(word)-1:
            return True 
        visit.add((i,j))
        if self.dfs(i+1,j,visit,word,board,count+1):
            return True
        if self.dfs(i-1,j,visit,word,board,count+1):
            return True
        if self.dfs(i,j+1,visit,word,board,count+1):
            return True
        if self.dfs(i,j-1,visit,word,board,count+1):
            return True
        visit.remove((i,j))

        return False        
