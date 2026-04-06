import bisect
import copy
import heapq
import os
from collections import defaultdict


def countLowerValueItems(items, startIndex, endIndex, query):
    # Write your code here
    unique_items = sorted(list(set(items)))
    item_frequency = defaultdict(int)
    freq_prefix = []
    for idx, item in enumerate(items):
        item_frequency[item] += 1
        freq_prefix.append(copy.deepcopy(item_frequency))

    ans = []
    order_count = len(startIndex)
    for q in query:
        # the keys less than q
        keys_less_than_q = unique_items[:bisect.bisect_left(unique_items, q)]
        count = 0
        for i in range(order_count):
            ss = startIndex[i]
            ee = endIndex[i]
            for k in keys_less_than_q:
                if ss == 0:
                    count += freq_prefix[ee][k]
                else:
                    count += freq_prefix[ee][k] - freq_prefix[ss - 1][k]
        ans.append(count)

    return ans


print(countLowerValueItems([1, 2, 3, 2, 4, 1], [2, 0], [4, 0], [5, 3]))
