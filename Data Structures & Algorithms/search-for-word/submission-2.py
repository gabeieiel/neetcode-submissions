class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m = len(board)      # quantidade de linhas
        n = len(board[0])   # quantidade de colunas       

        def dfs(i,j,p):
            '''
            dfs irá retornar True se encontramos a palavra a partir
            da letra board[i][j] == word[0] e falso c.c.
            '''

            if p == len(word): # p está em [0,n-1], então se chegou em n é porque já passou pela última letra
                return True

            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[p]:
                return False
            
            # suja a letra para não atrapalhar as buscas nas imediações
            letra_original = board[i][j]
            board[i][j] = "#"
                    
            # busca nas 4 direções
            encontrou = (dfs(i-1,j, p+1) or
                         dfs(i+1,j, p+1) or
                         dfs(i,j-1, p+1) or
                         dfs(i,j+1, p+1))
            
            # restaura a letra original após o fim das buscas
            board[i][j] = letra_original

            return encontrou

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i,j, 0):
                        return True
                
        return False
