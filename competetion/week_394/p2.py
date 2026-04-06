class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        have_upper = [False] * 26
        have_lower = [False] * 26
        special = [None] * 26
        for i in word:
            if i.isupper():
                have_upper[ord(i) - ord('A')] = True
                l = i.lower()
                if have_lower[ord(l) - ord('a')] and special[ord(l) - ord('a')] is None:
                    special[ord(l) - ord('a')] = True
            if i.islower():
                have_lower[ord(i) - ord('a')] = True
                u = i.upper()
                if have_upper[ord(u) - ord('A')]:
                    special[ord(u) - ord('A')] = False
        return special.count(True)


print(Solution().numberOfSpecialChars("cCceDC"))
