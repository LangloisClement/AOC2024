from functools import reduce, cmp_to_key
from pkg_resources import resource_stream

rules = []
printings = []
break_print = False
with resource_stream("input", "test.txt") as textInput:
    for line in textInput.readlines():
        line = line.decode().strip()
        if line == "":
            break_print = True
            continue
        if not break_print:
            before = int(line.split("|")[0])
            after = int(line.split("|")[1])
            rules.append((before, after))
        else:
            printings.append([int(i) for i in line.split(",")])


def compa(a, b):
    if (a, b) in rules:
        return 1
    elif (b, a) in rules:
        return -1
    else:
        1 / 0


def part1():
    valide_printing = []
    for printing in printings:
        if all((printing[i],printing[j]) in rules for i in range(len(printing)-1) for j in range(i+1,len(printing))):
            valide_printing.append(printing)
    return reduce(
        (lambda a, b: a + b),
        [printing[len(printing) // 2] for printing in valide_printing],
    )


def part2():
    pass