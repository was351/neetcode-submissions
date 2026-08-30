class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[set() for _ in range(len(board))]
        col=[set() for _ in range(len(board))]
        square=[set() for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board)):
                if board [i][j]==".":
                    continue
                sq_idx=i//3+j//3
                if board[i][j] in row[i]:
                    return False
                if board[i][j] in col[j]:
                    return False
                if board[i][j] in square[sq_indx]:
                    return False
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                square[sq_idx].add(board[i][j])
                
        return True
                
                
                
    