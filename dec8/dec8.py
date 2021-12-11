input = open("input.txt", "r")


def createCodeMap(pInput):
    segmentKeys = [""] * 10
    # find known numbers
    inputList = pInput.split()
    for x in inputList:
        length = len(x)
        if length == 2:
            segmentKeys[1] = x
        elif length == 4:
            segmentKeys[4] = x
        elif length == 3:
            segmentKeys[7] = x
        elif length == 7:
            segmentKeys[8] = x
    for key in segmentKeys:
        if key:
            inputList.remove(key)

    three = findThree(inputList, segmentKeys[1])
    segmentKeys[3] = three
    inputList.remove(three)

    nine = findNine(inputList, segmentKeys[4])
    segmentKeys[9] = nine
    inputList.remove(nine)

    zero = findZero(inputList, segmentKeys[1])
    segmentKeys[0] = zero
    inputList.remove(zero)

    six = findSix(inputList, segmentKeys[3])
    segmentKeys[6] = six
    inputList.remove(six)

    two = findTwo(inputList, segmentKeys[6])
    segmentKeys[2] = two
    inputList.remove(two)

    segmentKeys[5] = inputList[0]
    return segmentKeys


def removeCharacters(source, target):
    copySource = source
    for char in target:
        copySource = copySource.replace(char, "")
    return copySource


def containsSegments(source, target):
    return all([x in source for x in target])


def findThree(inputList, oneKey):
    for x in inputList:
        reducedLength = len(removeCharacters(x, oneKey))
        if containsSegments(x, oneKey) and reducedLength == 3:
            return x


def findNine(inputList, fourKey):
    for x in inputList:
        reducedLength = len(removeCharacters(x, fourKey))
        if containsSegments(x, fourKey) and reducedLength == 2:
            return x


def findZero(inputList, oneKey):
    for x in inputList:
        reducedLength = len(removeCharacters(x, oneKey))
        if containsSegments(x, oneKey) and reducedLength == 4:
            return x


def findSix(inputList, threeKey):
    for x in inputList:
        reducedLength = len(removeCharacters(x, threeKey))
        if reducedLength == 2:
            return x


def findTwo(inputList, sixKey):
    for x in inputList:
        reducedLength = len(removeCharacters(x, sixKey))
        if reducedLength == 1:
            return x


def decode(codeMap, toDecode: str):
    sortedCodeMap = ["".join(sorted(x)) for x in codeMap]
    result = ""
    for phrase in toDecode.split():
        sortedPhrase = "".join(sorted(phrase))
        for i in range(0, len(sortedCodeMap)):
            if sortedCodeMap[i] == sortedPhrase:
                result += str(i)
                break

    return int(result)


result = 0
for line in input:
    line = [x.strip() for x in line.split("|")]
    codeMap = createCodeMap(line[0])
    result += decode(codeMap, line[1])
print("Sum:", result)
