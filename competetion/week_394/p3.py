import sys
from collections import defaultdict
from functools import cache
from typing import List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        col_cost = defaultdict()
        # get col cost first
        for col in range(m):
            # each col
            col_dict = defaultdict(int)
            for i in range(n):
                col_dict[grid[i][col]] = n

            for row in range(n):
                col_dict[grid[row][col]] -= 1
            col_cost[col] = col_dict

        @cache
        def dp(i, j):
            if i == 0:
                return col_cost[0][j]
            ans = sys.maxsize
            for k in col_cost[i - 1].keys():
                if k != j:
                    ans = min(ans, col_cost[i][j] + dp(i - 1, k))
            if ans == sys.maxsize:
                ans = n + dp(i - 1, j)
            return ans

        res = sys.maxsize
        for k in col_cost[m - 1].keys():
            res = min(res, dp(m - 1, k))
        return res


print(Solution().minimumOperations([[3, 5, 2], [3, 5, 2], [1, 1, 1], [0, 0, 0]]))
print(Solution().minimumOperations([[2, 6, 6, 9, 8, 4, 2, 6, 2, 3]]))
print(Solution().minimumOperations([[4, 9, 2, 2, 3, 8, 1, 0, 9, 9]]))
