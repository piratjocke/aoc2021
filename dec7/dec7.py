def fuelCost(steps):
    return sum([x for x in range(1, steps+1)])


crabPos = [int(x) for x in open("input.txt", "r").read().split(",")]

minPos = min(crabPos)
maxPos = max(crabPos)
possiblePos = [x for x in range(minPos, maxPos+1)]

positionCost = {}
for toPos in possiblePos:
    if toPos not in positionCost:
        positionCost.setdefault(toPos, 0)
        for fromPos in crabPos:
            delta = fuelCost(abs(fromPos - toPos))
            positionCost[toPos] += delta
print(min(positionCost.values()))
