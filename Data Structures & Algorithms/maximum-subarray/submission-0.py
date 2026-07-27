class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        maxSum = nums[0]
        currentSum = 0

        for num in nums:
            if currentSum < 0: # não faz sentido somar um valor negativo
                currentSum = 0

            currentSum += num
            maxSum = max(maxSum, currentSum)

        return maxSum
