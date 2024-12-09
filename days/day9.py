from functools import reduce
from pkg_resources import resource_stream

disk_map = []
with resource_stream("input", "D9.txt") as textInput:
    for line in textInput.readlines():
        line = line.decode().strip()
        disk_map = [int(c) for c in line]
extand_disk = []
file_id = 0
for i in range(len(disk_map)):
    if i % 2 == 0:
        extand_disk += [file_id] * disk_map[i]
        file_id += 1
    else:
        extand_disk += ["."] * disk_map[i]


def right_shift(i):
    while type(extand_disk[i]) is not int:
        i -= 1
    return i


def part1():
    right_index = right_shift(len(extand_disk) - 1)
    left_index = 0
    while left_index < right_index:
        left_index += 1
        if type(extand_disk[left_index]) is int:
            continue
        extand_disk[left_index], extand_disk[right_index] = (
            extand_disk[right_index],
            extand_disk[left_index],
        )
        right_index = right_shift(right_index)
    ret = 0
    for i in range(right_index + 1):
        ret += extand_disk[i] * i
    return ret
