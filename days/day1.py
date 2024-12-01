from pkg_resources import resource_stream

def part1():
    listA, listB = [], []
    with resource_stream("input", "D1.txt") as textInput:
        for line in textInput.readlines():
            line = line.decode().strip()
            numbers = line.split()
            listA.append(int(numbers[0]))
            listB.append(int(numbers[1]))
    listA.sort()
    listB.sort()
    r = 0
    for i in range(len(listA)):
        r += abs(listA[i] - listB[i])
    return r
