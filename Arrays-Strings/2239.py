class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        answ = nums[0]
        dist = abs(0 - answ)
        for i in range(len(nums)):
            cur_dist = abs(0 - nums[i])
            if dist > cur_dist:
                answ = nums[i]
                dist = cur_dist
            if dist == cur_dist:
                answ = max(nums[i], answ)
        return answ

# Оптимизация
    def findClosestNumberFaster(self, nums: list[int]) -> int:
        answ = nums[0]
        for i in nums:
            if abs(i) < abs(answ):
                answ = i
        if answ < 0 and abs(answ) in nums:
            return abs(answ)
        else:
            return answ
