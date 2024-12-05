from pkg_resources import resource_stream
from collections import Counter

listA, listB = [], []
with resource_stream("input", "D1.txt") as textInput:
    for line in textInput.readlines():
        line = line.decode().strip()
        numbers = line.split()
        listA.append(int(numbers[0]))
        listB.append(int(numbers[1]))


def part1():
    listA.sort()
    listB.sort()
    r = 0
    for i in range(len(listA)):
        r += abs(listA[i] - listB[i])
    return r


def part2():
    count = Counter(listB)
    r = 0
    for n in listA:
        r += n * count[n]
    return r
