from functools import reduce
from pkg_resources import resource_stream


def part1():
    rules: dict[int : list[int]] = {}
    printings = []
    break_print = False
    with resource_stream("input", "D5.txt") as textInput:
        for line in textInput.readlines():
            line = line.decode().strip()
            if line == "":
                break_print = True
                continue
            if not break_print:
                before = int(line.split("|")[0])
                after = int(line.split("|")[1])
                if before not in rules:
                    rules[before] = [after]
                else:
                    rules[before].append(after)
            else:
                printings.append([int(i) for i in line.split(",")])
    valide_printing = []
    for printing in printings:
        invalide = False
        for i in range(len(printing)):
            afters = rules.get(printing[i], [])
            for j in range(i):
                if printing[j] in afters:
                    invalide = True
                    break
            if invalide:
                break
        if not invalide:
            valide_printing.append(printing)

    return reduce(
        (lambda a, b: a + b),
        [printing[len(printing) // 2] for printing in valide_printing],
    )
