from pkg_resources import resource_stream

reports: list[list[int]] = []
ret = 0
with resource_stream("input", "D2.txt") as textInput:
    for line in textInput.readlines():
        line = line.decode().strip()
        reports.append([int(num) for num in line.split()])


def reportSafe(report: list[int]):
    isAscending = report[0] < report[1]
    for i in range(len(report) - 1):
        if isAscending:
            if report[i] > report[i + 1]:
                return False
            if report[i + 1] - report[i] > 3 or report[i + 1] - report[i] < 1:
                return False
        else:
            if report[i] < report[i + 1]:
                return False
            if report[i] - report[i + 1] > 3 or report[i] - report[i + 1] < 1:
                return False
    return True


def part1():
    for report in reports:
        ret += 1 if reportSafe(report) else 0
    return ret


def part2():
    for report in reports:
        if reportSafe(report):
            ret += 1
            continue
        for i in range(len(report)):
            reportCopy = report.copy()
            reportCopy.pop(i)
            if reportSafe(reportCopy):
                ret += 1
                break

    return ret
