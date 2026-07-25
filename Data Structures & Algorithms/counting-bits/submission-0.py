class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # O estado atual é a contagem do número sem o seu último bit '1',
            # somado com +1 (representando o próprio bit que foi retirado).
            dp[i] = dp[i & (i - 1)] + 1
            
        return dp