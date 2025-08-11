from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new = set(nums)
        if len(new) == len(nums):
            return False
        else:
            return True


sol = Solution()
nums = [1, 2, 3, 4]
print(sol.containsDuplicate(nums))
