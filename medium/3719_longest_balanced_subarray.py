# -*- coding: utf-8 -*-
"""
Created on 10/02/2026 13:23

You are given an integer array nums.

A subarray is called balanced if the number of distinct even numbers in the subarray is equal to the number of distinct odd numbers.

Return the length of the longest balanced subarray.



Example 1:

Input: nums = [2,5,4,3]

Output: 4

Explanation:

The longest balanced subarray is [2, 5, 4, 3].
It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [5, 3]. Thus, the answer is 4.

@author: Aidan
@project: leetcode
@filename: 3719_longest_balanced_subarray
"""
from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        even_set = set()
        odd_set = set()
        ans = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[j] % 2 == 0:
                    even_set.add(nums[j])
                else:
                    odd_set.add(nums[j])
                if len(even_set) == len(odd_set):
                    ans = max(ans, j - i + 1)
            even_set.clear()
            odd_set.clear()

        return ans


print(Solution().longestBalanced(nums=[21, 17, 8, 9, 1]))
