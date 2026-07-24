class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        n = len(matrix[0])  # quantidade de colunas
        m = len(matrix)     # quantidade de linhas
        
        esquerda, direita = 0, len(matrix[0]) - 1
        topo, base = 0, len(matrix) - 1
        
        res = []
        
        while esquerda <= direita and topo <= base:

            # iterando sobre a linha (esq -> dir)            
            for col in range(esquerda, direita+1):
                res.append(matrix[topo][col])

            topo += 1           # desconsidera a linha recém iterada


            for linha in range(topo, base+1):
                # itera sobre as linhas adicionando sempre o limite máximo das linhas,
                # que é a coluna a ser iterada.              
                res.append(matrix[linha][direita])      

            direita -= 1        # desconsidera a coluna recém iterada


            if not (esquerda <= direita and topo <= base):
                break


            for col in range(direita, esquerda-1, -1):
                res.append(matrix[base][col])
            
            base -= 1


            for linha in range(base, topo-1, -1):
                # itera sobre as linhas adicionando sempre o limite mínimo das linhas,
                # que é a coluna a ser iterada.              
                res.append(matrix[linha][esquerda])

            esquerda += 1
    
        return res

