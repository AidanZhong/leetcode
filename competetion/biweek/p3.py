import sys
from collections import defaultdict, deque
from typing import List


class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        adj_dict = defaultdict(list)
        for u, v, w in edges:
            adj_dict[u].append((v, w))
            adj_dict[v].append((u, w))
        q = deque()
        q.append([0, 0])
        node_quickest = [sys.maxsize] * n
        while q:
            node, t = q.popleft()
            node_quickest[node] = min(t, node_quickest[node])
            for adj, cost in adj_dict[node]:
                if (t + cost < disappear[adj] and t + cost < node_quickest[adj]):
                    node_quickest[adj] = t + cost
                    q.append([adj, t + cost])
        for i in range(node_quickest.__len__()):
            if node_quickest[i] >= disappear[i]:
                node_quickest[i] = -1
        return node_quickest


print(Solution().minimumTime(n=3, edges=[[0, 1, 2], [1, 2, 1], [0, 2, 4]], disappear=[1, 1, 5]))
