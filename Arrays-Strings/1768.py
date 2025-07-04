class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        word_len1 = len(word1)
        word_len2 = len(word2)
        iterations = min(word_len1, word_len2)

        for i in range(iterations):
            merged += word1[i] + word2[i]

        if word_len2 > word_len1:
            merged += word2[iterations:]

        elif word_len2 < word_len1:
            merged += word1[iterations:]

        return merged


sol = Solution()
cor_answ = "apbqcd"
answ = sol.mergeAlternately("abcd", "pq")
print(cor_answ == answ)
