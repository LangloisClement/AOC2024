from pkg_resources import resource_stream


garden: list[list[str]] = []
with resource_stream("input", "D12.txt") as textInput:
    for line in textInput.readlines():
        line = line.decode().strip()
        garden.append(list(line))
L, C = len(garden), len(garden[0])


def get_region(i, j, region: set):
    region_type = garden[i][j]
    region.add((i, j))
    if i + 1 < L and garden[i + 1][j] == region_type and (i + 1, j) not in region:
        get_region(i + 1, j, region)
    if j + 1 < C and garden[i][j + 1] == region_type and (i, j + 1) not in region:
        get_region(i, j + 1, region)
    if i - 1 >= 0 and garden[i - 1][j] == region_type and (i - 1, j) not in region:
        get_region(i - 1, j, region)
    if j - 1 >= 0 and garden[i][j - 1] == region_type and (i, j - 1) not in region:
        get_region(i, j - 1, region)
    return region


def get_border(i, j):
    region_type = garden[i][j]
    ret = 0
    if i == L - 1 or i == 0:
        ret += 1
    if j == C - 1 or j == 0:
        ret += 1
    if i + 1 < L and garden[i + 1][j] != region_type:
        ret += 1
    if j + 1 < C and garden[i][j + 1] != region_type:
        ret += 1
    if i - 1 >= 0 and garden[i - 1][j] != region_type:
        ret += 1
    if j - 1 >= 0 and garden[i][j - 1] != region_type:
        ret += 1
    return ret


regions = []
seen = []
for i in range(L):
    for j in range(C):
        if (i, j) in seen:
            continue
        new_region = get_region(i, j, set())
        for cell in new_region:
            seen.append(cell)
        regions.append(new_region)


def part1():
    ret = 0
    for region in regions:
        border_size = 0
        for cell in region:
            border_size += get_border(*cell)
        ret += len(region) * border_size
    return ret
