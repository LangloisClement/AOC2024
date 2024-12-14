from re import findall
from importlib.resources import read_text

claws = []
text = read_text("input", "test.txt").split("\n")
for i in range(0, len(text), 4):
    button_A = tuple(map(int, findall(r"X\+(\d+), Y\+(\d+)", text[i])[0]))
    button_B = tuple(map(int, findall(r"X\+(\d+), Y\+(\d+)", text[i + 1])[0]))
    prize = tuple(map(int, findall(r"X=(\d+), Y=(\d+)", text[i + 2])[0]))
    claws.append((prize, button_A, button_B))


def part1():
    print(claws)
