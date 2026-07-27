class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1001] * n
        
        dp[0] = nums[0]     # a maior soma de 1 valor só é ele mesmo

        for i in range(1, n):
            '''
            a maior soma do valor em i é 
            max(ele próprio, a maior soma antes dele + ele)
            '''
            dp[i] = max(nums[i], dp[i-1] + nums[i])
        
        return max(dp)