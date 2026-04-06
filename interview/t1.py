# -*- coding: utf-8 -*-
"""
Created on 2025/9/20 14:56

@author: Aidan
@project: leetcode
@filename: t1
@description: 
- Python 
"""


class Tree:
    def __init__(self, x, children=None):
        self.x = x
        if not children:
            self.children = []
        else:
            self.children = children


def TreeConstructor(strArr):
    node_dict = dict()

    for i in strArr:
        pairs = i.split(',')
        child = pairs[0].lstrip("(")
        parent = pairs[1].rstrip(")")
        if child not in node_dict:
            node_dict[child] = Tree(child)
        if parent not in node_dict:
            node_dict[parent] = Tree(parent)

        node_dict[parent].children.append(node_dict[child])

    validated = set(node_dict.keys())

    def check(node: Tree):
        if len(node.children) > 2:
            return False
        for child in node.children:
            if not check(child):
                return False
        validated.add(node.x)
        return True

    for k, v in node_dict.items():
        if k in validated:
            continue
        if not check(v):
            return 'false'
    return 'true'


# keep this function call here
# print(TreeConstructor("[\"(1,2)\", \"(2,4)\", \"(5,7)\", \"(7,2)\", \"(9,5)\"]"))
print(TreeConstructor(["(1,2)", "(3,2)", "(2,12)", "(5,2)"]))
