class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visit=set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if self.rec(i,j,0,word,board,visit):
                        return True 
        return False 
    
    def rec(self,i,j,idx,word,board,visit):
        if idx>len(word):
            return True
        if i<0 or j<0 or i>=len(board)or j>=len(board[0]):
            return False
        if idx==len(word):
            return True 
        if (i,j) in visit:
            return False 
        if board[i][j]!=word[idx]:
            return False

        visit.add((i,j))
    
        if  self.rec(i+1,j,idx+1,word,board,visit):
            return True 
        if  self.rec(i-1,j,idx+1,word,board,visit):
            return True 
        if  self.rec(i,j-1,idx+1,word,board,visit):
            return True 
        if  self.rec(i,j+1,idx+1,word,board,visit):
            return True 
        visit.remove((i,j))
        return False 


        