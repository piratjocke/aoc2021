import math
from functools import reduce


def getNeighbours(index, heightMap, width):
    heightMapSize = len(heightMap)
    rowIndex = math.floor(index / width) * width
    top = index - width
    right = index + 1
    bottom = index + width
    left = index - 1
    neighbours = []

    if top >= 0:
        neighbours.append(top)
    if right < heightMapSize and right < rowIndex + width:
        neighbours.append(right)
    if bottom < heightMapSize:
        neighbours.append(bottom)
    if left >= 0 and left >= rowIndex:
        neighbours.append(left)
    return neighbours


def getBasin(index, heightMap, width, result):
    result.append(index)
    neighbours = getNeighbours(index, heightMap, width)
    for neighbour in neighbours:
        neighbourValue = int(heightMap[neighbour])
        currentValue = int(heightMap[index])
        if neighbourValue < 9 and currentValue < neighbourValue:
            getBasin(neighbour, heightMap, width, result)


input = open("input.txt", "r")

heightMap = input.read().split("\n")
mapWidth = len(heightMap[0])
heightMap = "".join(heightMap)
lowPoints = []
# find low points
for i in range(0, len(heightMap)):
    value = heightMap[i]
    if all([value < heightMap[x] for x in getNeighbours(i, heightMap, mapWidth)]):
        lowPoints.append(i)
# [1, 9, 22, 46]
basins = []
for x in lowPoints:
    result = []
    getBasin(x, heightMap, mapWidth, result)
    basins.append(set(result))
basinLengths = [len(x) for x in basins]
basinLengths.sort(reverse=True)
print(reduce(lambda x, y: x * y, basinLengths[:3]))
