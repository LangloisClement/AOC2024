from functools import reduce
from pkg_resources import resource_stream
from re import findall


def part1():
    ret = 0
    instruct = []
    with resource_stream("input", "D3.txt") as textInput:
        for line in textInput.readlines():
            line = line.decode().strip()
            instruct.append(findall(r"mul\((\d{1,3}),(\d{1,3})\)", line))
    for i in instruct:
        for t in i:
            ret += reduce((lambda x, y: int(x) * int(y)), t)

    return ret


def part2():
    ret = 0
    instruct = []
    with resource_stream("input", "D3.txt") as textInput:
        for line in textInput.readlines():
            line = line.decode().strip()
            instruct.append(findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line))
    enabled = True
    for i in instruct:
        for s in i:
            if s == "do()":
                enabled = True
            elif s == "don't()":
                enabled = False
            else:
                s = findall(r"mul\((\d{1,3}),(\d{1,3})\)", s)
                ret += reduce((lambda x, y: int(x) * int(y)), s[0]) if enabled else 0
    return ret
