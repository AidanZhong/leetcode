from collections import defaultdict


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0
        w_dict = [[False, False] for _ in range(26)]
        for char in word:
            if char.isupper():
                w_dict[ord(char) - ord('A')][0] = True
            if char.islower():
                w_dict[ord(char) - ord('a')][1] = True
        for i in range(26):
            if w_dict[i][0] and w_dict[i][1]:
                ans += 1
        return ans


