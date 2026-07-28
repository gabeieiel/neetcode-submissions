class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m = len(board)      # quantidade de linhas
        n = len(board[0])   # quantidade de colunas       

        p = 0

        def dfs(i,j,p):
            if p == len(word):
                return True

            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[p]:
                return False
            
            letra_original = board[i][j]
            board[i][j] = "#"
                    
            
            
            encontrou = (dfs(i-1,j, p+1) or
                         dfs(i+1,j, p+1) or
                         dfs(i,j-1, p+1) or
                         dfs(i,j+1, p+1))
            
            board[i][j] = letra_original

            return encontrou

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i,j, 0):
                        return True
                
        return False
