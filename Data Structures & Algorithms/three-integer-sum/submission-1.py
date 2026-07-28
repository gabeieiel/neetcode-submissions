class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        res = []

        for i in range(n):
            
            if nums[i] > 0:
                return res

            if i > 0 and nums[i] == nums[i-1]:
                continue    # pula para a próxima iteração
            
            j = i+1
            k = n-1

            if nums[i] == 0 and nums[j] == 0 and nums[k] == 0:
                res.append([nums[i], nums[j], nums[k]])
                return res

            while j < k:

                soma = nums[i] + nums[j] + nums[k]

                if soma < 0:
                    j += 1
                
                elif soma > 0:
                    k -= 1
                
                else:
                    res.append([nums[i], nums[j], nums[k]])

                    # buscando outros ponteiros para o mesmo i
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j-1]:
                        j += 1

        return res