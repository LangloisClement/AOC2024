from pkg_resources import resource_stream


def part1():
    reports: list[list[int]] = []
    ret=0
    with resource_stream("input", "D2.txt") as textInput:
        for line in textInput.readlines():
            line = line.decode().strip()
            reports.append([int(num) for num in line.split()])
    for report in reports:
        isAscending= report[0]<report[1]
        for i in range(len(report)-1):
            notSafe=False
            if isAscending:
                if report[i]>report[i+1]:
                    notSafe=True
                    break
                if report[i+1]-report[i]>3 or report[i+1]-report[i]<1:
                    notSafe=True
                    break
            else:
                if report[i]<report[i+1]:
                    notSafe=True
                    break
                if report[i]-report[i+1]>3 or report[i]-report[i+1]<1:
                    notSafe=True
                    break
                pass
        ret+=0 if notSafe else 1

    return ret
