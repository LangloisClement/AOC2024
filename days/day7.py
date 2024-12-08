from collections import Counter
import copy
from functools import reduce
from pkg_resources import resource_stream

equations: list[tuple[int, list[int]]] = []
with resource_stream("input", "D7.txt") as textInput:
    for line in textInput.readlines():
        line = line.decode().strip()
        res, nums = line.split(":")
        res = int(res)
        nums = [int(n) for n in nums.split()]
        equations.append((res, nums))


def is_incremant(target: int, nums: list[int], res: int = 0) -> bool:
    if res == target:
        return True
    if res > target or nums == []:
        return False
    if not is_incremant(target, nums[1:], res + nums[0]):
        return is_incremant(target, nums[1:], res * nums[0])
    else:
        return True


def part1():
    valide = [t for t in equations if is_incremant(t[0], t[1])]
    ret = 0
    for t in valide:
        ret += t[0]
    return ret


def part2():
    pass
