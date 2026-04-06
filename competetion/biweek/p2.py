from typing import List


class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points = sorted(list(set([points[i][0] for i in range(len(points))])))
        ptr = 0
        count = 1
        x_left = points[0]
        while ptr < len(points):
            if x_left + w >= points[ptr]:
                ptr += 1
                continue

            x_left = points[ptr]
            count += 1
            ptr += 1
        return count


print(Solution().minRectanglesToCoverPoints(points=[[2, 1], [1, 0], [1, 4], [1, 8], [3, 5], [4, 6]], w=1))
print(Solution().minRectanglesToCoverPoints(points=[[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]], w=2))
print(Solution().minRectanglesToCoverPoints(points=[[2, 3], [1, 2]], w=0))
