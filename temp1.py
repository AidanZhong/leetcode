# -*- coding: utf-8 -*-
"""
Created on 02/04/2026 15:27

@author: Aidan
@project: leetcode
@filename: temp1
"""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def grid_search_bfs(grid: list[list[int]], target: int) -> bool:
    # start at 0,0
    q = deque([(0, 0)])
    visited = set()
    while q:
        x, y = q.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if grid[x][y] == target:
            return True
        q.append((x + 1, y))
        q.append((x - 1, y))
        q.append((x, y + 1))
        q.append((x, y - 1))
