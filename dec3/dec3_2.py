import math


def convertBits(bits):
    return int("".join([str(x) for x in bits]), 2)


def findMostCommonBit(rows, position, inverse):
    result = 0
    nrOfRows = len(rows)
    for row in rows:
        result += int(row[position])
    result = math.floor(result / (nrOfRows/2))
    if inverse:
        return 1 if result == 0 else 0
    return result


def recursiveSearch(rows: list, position=0, inverse=False):
    result = findMostCommonBit(rows, position, inverse)
    filteredRows = list(filter(lambda x: int(x[position]) == result, rows))
    if len(filteredRows) > 1:
        return recursiveSearch(filteredRows, position+1, inverse)
    return filteredRows[0]


input = open("input.txt", "r")

reportLines = [line.rstrip("\n") for line in input]
oxygen = convertBits(recursiveSearch(reportLines))
c02 = convertBits(recursiveSearch(reportLines, inverse=True))
print(oxygen * c02)


# Find most common bit X on position N
# filter out lines starting with X
# repeat with position N+1
# be able to inverse
