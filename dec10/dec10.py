inputs = [x for x in open("input.txt", "r").read().split("\n")]

chunkPairs = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}
illegalPoints = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
autoCompletePoints = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}
syntaxScore = 0
incompleteLines = []
for line in inputs:
    lineCorrupted = False
    chunks = []
    for chunk in line:
        if chunk in chunkPairs.keys():
            chunks.append(chunk)
        elif chunk == chunkPairs[chunks[-1]]:
            chunks.pop()
        else:
            syntaxScore += illegalPoints[chunk]
            lineCorrupted = True
            break
    if not lineCorrupted:
        incompleteLines.append(line)

autoCompleteScores = []
for line in incompleteLines:
    chunks = []
    for chunk in line:
        if chunk in chunkPairs.keys():
            chunks.append(chunk)
        elif chunk == chunkPairs[chunks[-1]]:
            chunks.pop()
    autoCompleteScore = 0
    while chunks:
        chunk = chunks.pop()
        autoCompleteScore = (autoCompleteScore * 5) + \
            autoCompletePoints[chunkPairs[chunk]]
    autoCompleteScores.append(autoCompleteScore)

autoCompleteScores.sort()
finalAutoCompleteScore = autoCompleteScores[int(
    len(autoCompleteScores) / 2)]
print("Syntax score:", syntaxScore)
print("Autocomplete score:", finalAutoCompleteScore)
