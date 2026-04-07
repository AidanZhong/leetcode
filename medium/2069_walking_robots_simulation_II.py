# -*- coding: utf-8 -*-
"""
Created on 07/04/2026 09:38

@author: Aidan
@project: leetcode
@filename: 2069_walking_robots_simulation_II

A width x height grid is on an XY-plane with the bottom-left cell at (0, 0) and the top-right cell at (width - 1, height - 1). The grid is aligned with the four cardinal directions ("North", "East", "South", and "West"). A robot is initially at cell (0, 0) facing direction "East".

The robot can be instructed to move for a specific number of steps. For each step, it does the following.

Attempts to move forward one cell in the direction it is facing.
If the cell the robot is moving to is out of bounds, the robot instead turns 90 degrees counterclockwise and retries the step.
After the robot finishes moving the number of steps required, it stops and awaits the next instruction.

Implement the Robot class:

Robot(int width, int height) Initializes the width x height grid with the robot at (0, 0) facing "East".
void step(int num) Instructs the robot to move forward num steps.
int[] getPos() Returns the current cell the robot is at, as an array of length 2, [x, y].
String getDir() Returns the current direction of the robot, "North", "East", "South", or "West".
"""
from typing import List


class Robot:

    def __init__(self, width: int, height: int):
        self.grid = {"width": width, "height": height}
        self.pos = [0, 0]
        self.dir = 0
        self.dir_dict = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.dir_str = ["East", "North", "West", "South"]
        self.loop = height * 2 + width * 2 - 4

    def step(self, num: int) -> None:
        if num > 0 and num % self.loop == 0 and self.pos == [0, 0]:
            self.dir = 3
            return
        x, y = self.pos
        num %= self.loop
        if num == 0:
            return
        dx, dy = self.dir_dict[self.dir]
        dx *= num
        dy *= num
        if x + dx >= self.grid["width"] or x + dx < 0 or y + dy >= self.grid["height"] or y + dy < 0:
            # step limit
            step_limit = 0
            if self.dir == 0:
                step_limit = self.grid["width"] - x - 1
            elif self.dir == 1:
                step_limit = self.grid["height"] - y - 1
            elif self.dir == 2:
                step_limit = x
            elif self.dir == 3:
                step_limit = y
            # turn
            self.dir = (self.dir + 1) % 4
            self.pos = [min(max(x + dx, 0), self.grid["width"] - 1), min(max(y + dy, 0), self.grid["height"] - 1)]
            self.step(num - step_limit)
        else:
            self.pos = [min(max(x + dx, 0), self.grid["width"] - 1), min(max(y + dy, 0), self.grid["height"] - 1)]

    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return self.dir_str[self.dir]

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()

commands = ["Robot","getPos","getDir","step","step","step","step","step","step","step","step","getDir","getPos"]
args = [[97,98],[],[],[66392],[83376],[71796],[57514],[36284],[69866],[31652],[32038],[],[]]
obj = None
for i in range(len(commands)):
    if commands[i] == "Robot":
        obj = Robot(*args[i])
    elif commands[i] == "step":
        print(obj.step(*args[i]))
    elif commands[i] == "getPos":
        print(obj.getPos())
    elif commands[i] == "getDir":
        print(obj.getDir())

