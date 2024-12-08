from pkg_resources import resource_stream


grid: list[list[str]] = []
with resource_stream("input", "test.txt") as textInput:
    for line in textInput.readlines():
        line = line.decode().strip()
        grid.append(list(line))
L, C = len(grid), len(grid[0])

antennas: dict[str : list[tuple[int, int]]] = {}
for i in range(L):
    for j in range(C):
        frequency = grid[i][j]
        if frequency != ".":
            if frequency not in antennas:
                antennas[frequency] = []
            antennas[frequency].append((i, j))


def part1():
    antinodes = set()
    for freq, pos in antennas.items():
        for i in range(len(pos)):
            for j in range(i + 1, len(pos)):
                x1, y1 = pos[i]
                x2, y2 = pos[j]
                dx = x2 - x1
                dy = y2 - y1

                ax1 = x1 + 2 * dx
                ay1 = y1 + 2 * dy

                ax2 = x2 - 2 * dx
                ay2 = y2 - 2 * dy
                if 0 <= ax1 < L and 0 <= ay1 < C:
                    antinodes.add((round(ax1), round(ay1)))
                if 0 <= ax2 < L and 0 <= ay2 < C:
                    antinodes.add((round(ax2), round(ay2)))
    return len(antinodes)


# def part2():
#     antinodes = set()
#     for freq, pos in antennas.items():
#         for i in range(len(pos)):
#             for j in range(i + 1, len(pos)):
#                 x1, y1 = pos[i]
#                 x2, y2 = pos[j]
#                 dx = x2 - x1
#                 dy = y2 - y1
#                 ax1 = x1 + 2 * dx
#                 ay1 = y1 + 2 * dy
#                 in_bound = 0 <= ax1 < L and 0 <= ay1 < C
#                 while in_bound:
#                     antinodes.add((round(ax1), round(ay1)))
#                     ax1 = ax1 + 2 * dx
#                     ay1 = ay1 + 2 * dy
#                     in_bound = 0 <= ax1 < L and 0 <= ay1 < C
#                 ax2 = x2 + 2 * dx
#                 ay2 = y2 + 2 * dy
#                 in_bound = 0 <= ax2 < L and 0 <= ay2 < C
#                 while in_bound:
#                     antinodes.add((round(ax2), round(ay2)))
#                     ax2 = ax2 + 2 * dx
#                     ay2 = ay2 + 2 * dy
#                     in_bound = 0 <= ax2 < L and 0 <= ay2 < C

#     return len(antinodes)
