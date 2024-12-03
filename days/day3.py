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
