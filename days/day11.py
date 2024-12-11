from pkg_resources import resource_stream

rock_line=[]
with resource_stream("input", "test.txt") as textInput:
    for line in textInput.readlines():
        line = line.decode().strip()
        rock_line = [int(c) for c in line.split()]


def part1():
    #Python being weird and not allowing global var...
    rock_line=[]
    with resource_stream("input", "D11.txt") as textInput:
        for line in textInput.readlines():
            line = line.decode().strip()
            rock_line = [int(c) for c in line.split()]
    new_rock_line = []
    for _ in range(25):
        new_rock_line = []
        for rock in rock_line:
            if rock == 0:
                new_rock_line.append(1)
                continue
            if len(str(rock)) % 2 == 0:
                a, b = (
                    str(rock)[: len(str(rock)) // 2],
                    str(rock)[len(str(rock)) // 2 :],
                )
                new_rock_line.append(int(a))
                new_rock_line.append(int(b))
                continue
            new_rock_line.append(2024 * rock)
        rock_line = new_rock_line.copy()
    return len(rock_line)
