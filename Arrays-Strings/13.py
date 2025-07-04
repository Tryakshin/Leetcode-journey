class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        translate = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        prev = translate.get(s[0], 0)

        if len(s) == 1:
            return answer + prev
        for i in range(1, len(s)):
            curr = translate.get(s[i], 0)
            if prev < curr:
                answer -= prev
                prev = curr
            else:
                answer += prev
                prev = curr

        return answer + prev


sol = Solution()
answer = 1994
s = "MCMXCIV"
print(sol.romanToInt(s) == answer)
