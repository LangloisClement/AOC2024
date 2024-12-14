from re import findall
from pkg_resources import resource_stream


robots = []
with resource_stream("input", "D14.txt") as textInput:
    for line in textInput.readlines():
        line = line.decode().strip()
        regex = findall(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line)
        robots.append([int(x) for x in regex[0]])


def part1():
    C = 101
    L = 103
    q_up_left = 0
    q_up_right = 0
    q_down_left = 0
    q_down_right = 0
    for robot in robots:
        robot[0] = (robot[0] + robot[2] * 100) % C
        robot[1] = (robot[1] + robot[3] * 100) % L
        if 0 <= robot[0] < C // 2 and 0 <= robot[1] < L // 2:
            q_up_left += 1
        elif C // 2 < robot[0] < C and 0 <= robot[1] < L // 2:
            q_up_right += 1
        elif 0 <= robot[0] < C // 2 and L // 2 < robot[1] < L:
            q_down_left += 1
        elif C // 2 < robot[0] < C and L // 2 < robot[1] < L:
            q_down_right += 1
        else:
            pass
    return q_up_left * q_up_right * q_down_left * q_down_right
