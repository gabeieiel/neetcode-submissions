class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        
        for _ in range(32):
            # extrai o bit menos significativo de n
            bit = n & 1
            
            # desloca res para a esquerda e insere o bit
            res = (res << 1) | bit
            
            # Desloca n para a direita para descartar o bit processado
            n >>= 1
            
        return res