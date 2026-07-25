class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        
        
        for i in range(1, n + 1):
            # [i>>1] desloca todos os bits de bin(i) 1 casa à direita
            # (i & 1) retorna 1 se o número for ímpar, 0 c.c.
            dp[i] = dp[i >> 1] + (i & 1)
            
        return dp