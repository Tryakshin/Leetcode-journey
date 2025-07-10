from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base = min(strs)
        ch_index = 0
        flag = True
        while flag and ch_index != len(base):
            for i in strs:
                if i[ch_index] != base[ch_index]:
                    flag = False
                    break
            if flag:
                ch_index += 1
            else:
                break
        return base[:ch_index]


sol = Solution()
strs = ["dog", "racecar", "car"]
print(sol.longestCommonPrefix(strs))
