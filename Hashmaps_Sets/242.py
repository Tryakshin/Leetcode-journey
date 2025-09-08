from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = Counter(s)
        t_map = Counter(t)

        if s_map == t_map:
            return True
        else:
            return False


s = "cat"
t = "nagaram"
sol = Solution()
print(sol.isAnagram(s, t))
