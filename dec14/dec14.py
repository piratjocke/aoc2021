import re


def evenFasterPolymer(polymerPairs, template, steps):
    elements = {}
    pairs = {}

    for x in polymerPairs.keys():
        pairs.setdefault(x, 0)

    for x in range(0, len(template)-1):
        key = template[x:x+2]
        pairs[key] += 1

    for x in range(0, steps):
        newPairs = {}
        for key in pairs:
            occurences = pairs[key]
            if occurences > 0:
                newLetter = polymerPairs[key]
                elements[newLetter] = elements.setdefault(
                    newLetter, 0) + occurences
                pairOne = key[0] + newLetter
                pairTwo = newLetter + key[1]
                newPairs[pairOne] = newPairs.setdefault(
                    pairOne, 0) + occurences
                newPairs[pairTwo] = newPairs.setdefault(
                    pairTwo, 0) + occurences
                pairs[key] = 0
        for key in newPairs:
            pairs[key] += newPairs[key]
    return elements


instructions = open("input.txt", "r")

pairPattern = re.compile("^(\w+) -> (\w+)$")

template = instructions.readline().rstrip()
# remove empty space
instructions.readline()
polymerPairs = {}
for pair in instructions:
    match = pairPattern.match(pair.rstrip())
    polymerPairs[match[1]] = match[2]

result = evenFasterPolymer(polymerPairs, template, 40)
print(result)
for x in template:
    result[x] += 1
values = list(result.values())
values.sort()
print(values)
print("Result:", values[-1] - values[0])
