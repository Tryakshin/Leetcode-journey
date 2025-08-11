class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Сделаем из строки множество что бы убрать повторяющиеся символы
        s = set(jewels)
        answer = 0
        for i in stones:
            if i in s:
                answer += 1

        return answer


jewels = "Aa"
stones = "Aaabbbbbbbbb"
sol = Solution()
print(sol.numJewelsInStones(jewels, stones))
