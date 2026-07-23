class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        soma_total = 0
        
        soma_parcial = sum(nums)

        for i in range(n):
            soma_total += i+1 

        return soma_total - soma_parcial