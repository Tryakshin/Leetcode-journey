from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        baloon_map = Counter("balloon")
        target_map = Counter(text)

        answer = float("inf")
        for key, value in baloon_map.items():
            if key not in target_map:
                return 0
            else:
                quantity_of_chars = target_map[key] // value
                answer = min(answer, quantity_of_chars)
        return answer


sol = Solution()

print(sol.maxNumberOfBalloons("nlaebolko"))