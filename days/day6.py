from collections import Counter
from functools import reduce
from pkg_resources import resource_stream


plan: list[list[str]] = []
with resource_stream("input", "D6.txt") as textInput:
    for line in textInput.readlines():
        line = line.decode().strip()
        plan.append(list(line))
DIRECTION = ["UP", "RIGHT", "DOWN", "LEFT"]
L, C = len(plan), len(plan[0])


def get_pos():
    for i in range(len(plan)):
        for j in range(len(plan[0])):
            if plan[i][j] == "^":
                return [i, j]


def part1():
    position = get_pos()
    facing = 0
    is_out = False
    while not is_out:
        ahead = position.copy()
        match DIRECTION[facing]:
            case "UP":
                ahead[0] -= 1
            case "RIGHT":
                ahead[1] += 1
            case "DOWN":
                ahead[0] += 1
            case "LEFT":
                ahead[1] -= 1
            case _:
                raise Exception
        if ahead[0] < 0 or ahead[0] >= L or ahead[1] < 0 or ahead[1] >= C:
            plan[position[0]][position[1]] = "X"
            is_out = True
            continue
        match plan[ahead[0]][ahead[1]]:
            case "#":
                facing = (facing + 1) % 4
            case _:
                plan[position[0]][position[1]] = "X"
                position = ahead
    return reduce((lambda a, b: a + b), [Counter(s)["X"] for s in plan])
