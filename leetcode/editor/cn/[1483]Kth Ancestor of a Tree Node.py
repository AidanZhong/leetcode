# You are given a tree with n nodes numbered from 0 to n - 1 in the form of a 
# parent array parent where parent[i] is the parent of iᵗʰ node. The root of the 
# tree is node 0. Find the kᵗʰ ancestor of a given node. 
# 
#  The kᵗʰ ancestor of a tree node is the kᵗʰ node in the path from that node 
# to the root node. 
# 
#  Implement the TreeAncestor class: 
# 
#  
#  TreeAncestor(int n, int[] parent) Initializes the object with the number of 
# nodes in the tree and the parent array. 
#  int getKthAncestor(int node, int k) return the kᵗʰ ancestor of the given 
# node node. If there is no such ancestor, return -1. 
#  
# 
#  
#  Example 1: 
#  
#  
# Input
# ["TreeAncestor", "getKthAncestor", "getKthAncestor", "getKthAncestor"]
# [[7, [-1, 0, 0, 1, 1, 2, 2]], [3, 1], [5, 2], [6, 3]]
# Output
# [null, 1, 0, -1]
#  
# 
# Explanation
# TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);
# treeAncestor.getKthAncestor(3, 1); // returns 1 which is the parent of 3
# treeAncestor.getKthAncestor(5, 2); // returns 0 which is the grandparent of 5
# treeAncestor.getKthAncestor(6, 3); // returns -1 because there is no such 
# ancestor
# 
#  
#  Constraints: 
# 
#  
#  1 <= k <= n <= 5 * 10⁴ 
#  parent.length == n 
#  parent[0] == -1 
#  0 <= parent[i] < n for all 0 < i < n 
#  0 <= node < n 
#  There will be at most 5 * 10⁴ queries. 
#  
# 
#  Related Topics 树 深度优先搜索 广度优先搜索 设计 二分查找 动态规划 👍 221 👎 0
import math
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.deepest = 16
        self.ancestor = [[-1] * self.deepest for _ in range(n)]
        for i in range(n):
            self.ancestor[i][0] = parent[i]
        for j in range(1, self.deepest):
            for i in range(n):
                if self.ancestor[i][j - 1] == -1:
                    self.ancestor[i][j] = -1
                else:
                    self.ancestor[i][j] = self.ancestor[self.ancestor[i][j - 1]][j - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        if node == -1:
            return -1
        s = bin(k)[2:][::-1]
        for i in range(s.__len__()):
            if s[i] == '1':
                node = self.ancestor[node][i]
                if node == -1:
                    return -1
        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
# leetcode submit region end(Prohibit modification and deletion)
obj = TreeAncestor(6, [-1, 2, 3, 4, 5, 0])
print(obj.getKthAncestor(1, 4))
