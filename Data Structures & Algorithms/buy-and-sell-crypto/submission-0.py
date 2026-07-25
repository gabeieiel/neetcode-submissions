class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        esq, dir = 0, 1    # ponteiros no array
        lucro_max   = 0

        while dir < n:
            if prices[esq] >= prices[dir]:
                esq = dir
                dir += 1
            
            else:
                lucro_max = max(lucro_max, prices[dir] - prices[esq])
                dir += 1
                
        return lucro_max
