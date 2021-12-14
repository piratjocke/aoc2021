def boxFilter(index, width, gridSize):
    rowStartIndex = int(index / width) * width
    rowEndIndex = int(index / width) * width + width

    neighbours = []
    for y in range(-1, 2):
        for x in range(-1, 2):
            currentIndex = (index + y * width) + x
            if index != currentIndex and currentIndex >= 0 and currentIndex >= (rowStartIndex + y * width) and currentIndex < (rowEndIndex + y * width) and currentIndex < gridSize:
                neighbours.append(currentIndex)
    return neighbours


def flashOctopus(grid, index, width, gridSize):
    if grid[index] != -1:
        grid[index] += 1
        if grid[index] > 9:
            # flash
            grid[index] = -1
            # flash neighbours
            neighbours = boxFilter(index, width, gridSize)
            for i in neighbours:
                flashOctopus(grid, i, width, gridSize)


input = open("input.txt", "r").read().split("\n")
gridWidth = len(input[0])
gridHeight = len(input)
gridSize = gridWidth * gridHeight
grid = [int(x) for x in "".join(input)]

firstSyncedFlash = 0
while True:
    firstSyncedFlash += 1
    flashes = 0
    for i in range(0, gridSize):
        flashOctopus(grid, i, gridWidth, gridSize)
    for i in range(0, gridSize):
        if grid[i] == -1:
            flashes += 1
            grid[i] = 0
    if flashes == 100:
        break
print(firstSyncedFlash)
