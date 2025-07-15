from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        left_product = 1
        for i in range(n):
            answer[i] = left_product 
            left_product *= nums[i]

        right_product = 1
        for j in range(n-1, -1, -1):
            answer[j] *= right_product
            right_product *= nums[j]

        return answer


print(Solution().productExceptSelf(nums=[-1, 1, 0, -3, 3]))
