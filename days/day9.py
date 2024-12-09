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
    while type(extand_disk[i]) is not int and i > 0:
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


def get_left_block_index(mem, RIGHT_INDEX):
    i = 0
    while extand_disk[mem + i] == extand_disk[mem] and i < RIGHT_INDEX:
        i += 1
    return mem + i


def get_right_block_index(mem):
    i = 0
    while extand_disk[mem - i] == extand_disk[mem]:
        i += 1
    return mem - i


def part2():
    right_index = right_shift(len(extand_disk) - 1)
    while right_index > 0:
        right_block_index = get_right_block_index(right_index)
        left_index = 0
        change = False
        while left_index < right_block_index:
            if type(extand_disk[left_index]) is int:
                left_index += 1
                continue
            left_block_index = get_left_block_index(left_index, right_index)
            if left_block_index - left_index >= right_index - right_block_index:
                for i in range(right_index - right_block_index):
                    (
                        extand_disk[left_index + i],
                        extand_disk[right_block_index + i + 1],
                    ) = (
                        extand_disk[right_block_index + i + 1],
                        extand_disk[left_index + i],
                    )
                right_index = right_shift(right_index)
                change = True
                break
            else:
                left_index += 1
        if not change:
            right_index = right_shift(right_block_index)
    ret = 0
    right_index = right_shift(len(extand_disk) - 1)
    for i in range(right_index + 1):
        ret += extand_disk[i] * i if type(extand_disk[i]) is int else 0
    return ret
