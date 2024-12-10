from pkg_resources import resource_stream


grid: list[list[int]] = []
with resource_stream("input", "D10.txt") as textInput:
    for line in textInput.readlines():
        line = line.decode().strip()
        grid.append([int(c) for c in line])
L, C = len(grid), len(grid[0])

trail_heads = [(i, j) for i in range(L) for j in range(C) if grid[i][j] == 0]


def traverse_trail(i, j):
    current = grid[i][j]
    ret2 = set()
    if current == 9:
        return (i, j)
    if i + 1 < L and grid[i + 1][j] == current + 1:
        res = traverse_trail(i + 1, j)
        if type(res) is tuple:
            ret2.add(res)
        else:
            ret2.update(res)
    if j + 1 < C and grid[i][j + 1] == current + 1:
        res = traverse_trail(i, j + 1)
        if type(res) is tuple:
            ret2.add(res)
        else:
            ret2.update(res)
    if i - 1 >= 0 and grid[i - 1][j] == current + 1:
        res = traverse_trail(i - 1, j)
        if type(res) is tuple:
            ret2.add(res)
        else:
            ret2.update(res)
    if j - 1 >= 0 and grid[i][j - 1] == current + 1:
        res = traverse_trail(i, j - 1)
        if type(res) is tuple:
            ret2.add(res)
        else:
            ret2.update(res)
    return ret2


def part1():
    trails = []
    for trail_head in trail_heads:
        trails.append(traverse_trail(*trail_head))
    ret = 0
    for trail in trails:
        ret += len(trail)
    return ret
