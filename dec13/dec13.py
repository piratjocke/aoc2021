def create2DArray(width, height):
    return [[0 for i in range(height)] for j in range(width)]


def printPaper(paper):
    width = len(paper)
    height = len(paper[0])
    print("=" * width)
    for col in range(0, height):
        strRow = ""
        for row in range(0, width):
            strRow += "." if paper[row][col] == 0 else "#"
        print(strRow)


def foldPaper(paper, dir, line):
    width = len(paper)
    height = len(paper[0])
    if dir == "y":
        newHeight = line
        newPaper = create2DArray(width, newHeight)
        for x in range(0, width):
            for y in range(0, newHeight):
                newPaper[x][y] = paper[x][y]

        nrOfFoldRows = height - (line + 1)
        for x in range(0, width):
            for y in range(0, nrOfFoldRows):
                adjustedY = newHeight - nrOfFoldRows + y
                invertedY = line + nrOfFoldRows - y
                newPaper[x][adjustedY] += paper[x][invertedY]
        return newPaper

    if dir == "x":
        newWidth = line
        newPaper = create2DArray(newWidth, height)
        for x in range(0, newWidth):
            for y in range(0, height):
                newPaper[x][y] = paper[x][y]

        nrOfFoldCols = width - (line + 1)
        for x in range(0, nrOfFoldCols):
            for y in range(0, height):
                adjustedX = newWidth - nrOfFoldCols + x
                invertedX = line + nrOfFoldCols - x
                newPaper[adjustedX][y] += paper[invertedX][y]
        return newPaper
    return paper


instructions = open("input.txt", "r").read()
splitInstructions = instructions.split("\n\n")

paperWidth = 0
paperHeight = 0
coords = []
for mark in splitInstructions[0].split("\n"):
    markCoords = [int(x) for x in mark.rstrip().split(",")]
    paperWidth = max(paperWidth, markCoords[0] + 1)
    paperHeight = max(paperHeight, markCoords[1] + 1)
    coords.append(markCoords)

startingWidth = paperWidth
paper = create2DArray(paperWidth, paperHeight)

for coord in coords:
    x = coord[0]
    y = coord[1]
    paper[x][y] = 1

folds = []
for fold in splitInstructions[1].splitlines():
    foldInstructions = fold.split()[2].split("=")
    foldInstructions[1] = int(foldInstructions[1])
    folds.append(foldInstructions)

for fold in folds:
    paper = foldPaper(paper, fold[0], fold[1])
    printPaper(paper)
