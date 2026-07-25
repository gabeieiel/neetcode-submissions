class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
            
        m = len(grid)       # quantidade de linhas
        n = len(grid[0])    # quantidade de colunas
        ilhas = 0
        
        # função dfs recursiva
        def dfs(i, j):
            # saindo dos limites da matriz ou bater na água
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
                return
            
            # marca a terra atual como visitada
            grid[i][j] = "0"
            
            # 3. Propaga a DFS estritamente nas 4 direções válidas
            dfs(i - 1, j) # Cima
            dfs(i + 1, j) # Baixo
            dfs(i, j - 1) # Esquerda
            dfs(i, j + 1) # Direita

        # Varredura principal
        for i in range(m):
            for j in range(n):
                # Achou um pedaço de terra? É uma ilha nova.
                if grid[i][j] == "1":
                    ilhas += 1
                    # Dispara a DFS para afundar o resto dessa ilha específica
                    dfs(i, j) 
                    
        return ilhas