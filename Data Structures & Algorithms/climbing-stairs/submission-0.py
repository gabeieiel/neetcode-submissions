class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)    # placeholder 0 para não colocar nenhum valor falso
        dp[0] = 1           # há 1 maneira de subir uma escada de 0 degraus: ficando parado

        steps = [1,2]

        for i in range(1,n+1):
            for step in steps:
                # sendo o step atual válido...
                if (i - step) >= 0:
                    '''
                    a forma de chegar no degrau i é
                        todas as formas de chegar no degrau i-1
                        +
                        todas as formas de chegar no degrau i-2
                    '''
                    dp[i] +=  dp[i-step]
        
        return dp[n]