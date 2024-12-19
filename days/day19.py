from re import findall
from importlib.resources import read_text

paterns = []
text = read_text("input", "D19.txt").split("\n")
paterns = [s.strip() for s in text[0].split(",")]
paterns.sort(key=len, reverse=True)
designs = text[2:]


def part1():
    ret = 0
    for design in designs:
        valide = True
        while valide:
            change = False
            for patern in paterns:
                if design.startswith(patern):
                    design = design.removeprefix(patern)
                    change = True
                    break
            if len(design) == 0:
                ret += 1
                valide = False
            if not change:
                break
    return ret
