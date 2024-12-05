from functools import reduce
from pkg_resources import resource_stream
from re import findall


def part1():
    ret = 0
    matrice = []
    with resource_stream("input", "D4.txt") as textInput:
        for line in textInput.readlines():
            line = line.decode().strip()
            matrice.append(line)
    # horizontal
    for l in range(len(matrice)):
        for c in range(len(matrice[l]) - 3):
            mask = [matrice[l][c + i] for i in range(4)]
            ret += 1 if mask == list("XMAS") or mask == list("SAMX") else 0
    # vertical
    for c in range(len(matrice[0])):
        for l in range(len(matrice) - 3):
            mask = [matrice[l + i][c] for i in range(4)]
            ret += 1 if mask == list("XMAS") or mask == list("SAMX") else 0
    # diagon down
    for c in range(len(matrice[0]) - 3):
        for l in range(len(matrice) - 3):
            mask = [matrice[l + i][c + i] for i in range(4)]
            ret += 1 if mask == list("XMAS") or mask == list("SAMX") else 0
    # diagon up
    for c in range(3, len(matrice[0])):
        for l in range(len(matrice) - 3):
            mask = [matrice[l + i][c - i] for i in range(4)]
            ret += 1 if mask == list("XMAS") or mask == list("SAMX") else 0
    return ret


def part2():
    ret = 0
    matrice = []
    with resource_stream("input", "D4.txt") as textInput:
        for line in textInput.readlines():
            line = line.decode().strip()
            matrice.append(line)
    for l in range(len(matrice) - 2):
        for c in range(len(matrice[0]) - 2):
            grid = [[matrice[l + i][c + j] for j in range(3)] for i in range(3)]
            if grid[1][1] == "A":
                if (grid[0][0] == "M" and grid[2][2] == "S") and (
                    grid[2][0] == "M" and grid[0][2] == "S"
                ):
                    ret += 1
                if (grid[0][0] == "S" and grid[2][2] == "M") and (
                    grid[2][0] == "S" and grid[0][2] == "M"
                ):
                    ret += 1
                if (grid[0][0] == "M" and grid[2][2] == "S") and (
                    grid[2][0] == "S" and grid[0][2] == "M"
                ):
                    ret += 1
                if (grid[0][0] == "S" and grid[2][2] == "M") and (
                    grid[2][0] == "M" and grid[0][2] == "S"
                ):
                    ret += 1
    return ret
