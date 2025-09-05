from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = Counter(magazine)

        for i in ransomNote:
            if hashmap[i] > 0:
                hashmap[i] -= 1
            else:
                return False
        return True
