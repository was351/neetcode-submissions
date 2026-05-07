class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    visit=set()
                    if self.find(i,j,0,visit,board,word):
                        return True
                    
        return False
    def find(self,i,j,idx,visit,board,word):
        if i>=len(board)or j>=len(board[0])or j<0 or i<0:
            return False
        if board[i][j]!=word[idx]:
            return False
        if (i,j) in visit:
            return False
        if idx==len(word)-1:
            return True
        visit.add((i,j))
        if self.find(i+1,j,idx+1,visit,board,word):
            return True
        if self.find(i-1,j,idx+1,visit,board,word):
            return True 
        if self.find(i,j+1,idx+1,visit,board,word):
            return True 
        if self.find(i,j-1,idx+1,visit,board,word):
            return True 
        visit.remove((i,j))
        return False
        
        