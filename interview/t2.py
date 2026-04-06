# -*- coding: utf-8 -*-
"""
Created on 2025/9/20 15:27

@author: Aidan
@project: leetcode
@filename: t2
@description: 
- Python 
"""
from collections import deque


def BitmapHoles(strArr):
  visited = set()
  n = len(strArr)
  m = len(strArr[0])
  count = 0
  for i in range(n):
    for j in range(m):
      if strArr[i][j] == '0' and (i, j) not in visited:
        visited.add((i, j))
        count += 1
        # bfs
        q = deque()
        q.append((i, j))
        while q:
          x, y = q.popleft()
          # up
          if x > 0 and (x-1, y) not in visited and strArr[x - 1][y] == '0':
            visited.add((x-1, y))
            q.append((x-1, y))
          # down
          if x < n - 1 and (x+1, y) not in visited and strArr[x + 1][y] == '0':
            visited.add((x+1, y))
            q.append((x+1, y))
          # left
          if y > 0 and (x, y-1) not in visited and strArr[x][y - 1] == '0':
            visited.add((x, y-1))
            q.append((x, y-1))
          # right
          if y < m - 1 and (x, y+1) not in visited and strArr[x][y+1] == '0':
            visited.add((x, y+1))
            q.append((x, y+1))

  # code goes here
  return count