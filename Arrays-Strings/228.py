from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answ = []
        if len(nums) == 0:
            return answ
        slow = fast = 0
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i] - 1:
                fast = i
            else:
                if fast == slow:
                    answ.append(str(nums[fast]))
                    fast = slow = i
                else:
                    answ.append(f"{nums[slow]}->{nums[fast]}")
                    fast = slow = i
        if fast == slow:
            answ.append(str(nums[fast]))
        else:
            answ.append(f"{nums[slow]}->{nums[fast]}")
        return answ


sol = Solution()
nums = [0, 1, 2, 4, 5, 7]
print(sol.summaryRanges(nums))
