import math


def convertBits(bits):
    return int("".join([str(x) for x in bits]), 2)


input = open("input.txt", "r")
result = [0] * len(input.readline().rstrip("\n"))

input.seek(0)
reportLength = 0
for line in input:
    for x in range(0, len(line.rstrip("\n"))):
        result[x] += int(line[x])
    reportLength += 1
for x in range(0, len(result)):
    result[x] = math.floor(result[x] / (reportLength/2))
gamma = convertBits(result)
epsilon = convertBits([1 if x == 0 else 0 for x in result])
print(epsilon * gamma)
