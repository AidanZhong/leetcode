# -*- coding: utf-8 -*-
"""
Created on 17/02/2026 11:15

@author: Aidan
@project: leetcode
@filename: 401_bin_watch
"""
import math
from functools import cache
from typing import List


@cache
def convert_bin_2_time(bin_num: int) -> str:
    """Converts binary number to valid time string"""
    s = bin(bin_num)[2:].zfill(10)
    hour = 0
    minute = 0
    for idx, i in enumerate(s):
        if i == '0':
            continue
        if idx <= 3:
            hour += 2 ** (3 - idx)
        else:
            minute += 2 ** (9 - idx)
    if hour > 11 or minute > 59:
        return None
    return f"{hour}:{minute:02d}"


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        for num in range(2 ** 10):
            if bin(num).count('1') != turnedOn:
                continue
            if convert_bin_2_time(num) is None:
                continue
            ans.append(convert_bin_2_time(num))
        return ans


print(Solution().readBinaryWatch(1))
