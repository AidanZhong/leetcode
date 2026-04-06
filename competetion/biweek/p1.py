class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for i in range(1, s.__len__()):
            ans += abs(ord(s[i]) - ord(s[i - 1]))
        return ans


print(Solution().scoreOfString(s="hello"))
