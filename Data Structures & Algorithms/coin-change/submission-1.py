class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1,amount+1):

            for c in coins:

                if (i-c) >= 0:  # i-c é o troco na iteração atual com a moeda c
                    dp[i] = min(dp[i], 1+dp[i-c])  # 1 + dp[i-c] é a moeda atual + a quantidade de moedas do troco i-c

        return dp[amount] if (dp[amount] != amount+1) else -1