class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        soma_total = 0
        
        soma_parcial = sum(nums)

        for i in range(1, n+1):
            soma_total += i 

        return soma_total - soma_parcial