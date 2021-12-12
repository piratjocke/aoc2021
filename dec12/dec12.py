import re


def getPaths(caveMap, fromNode, pathTaken, possiblePaths, doubleVisitNode=None):
    currentPath = pathTaken[:]
    currentPath.append(fromNode)
    # actual end
    if fromNode == "end":
        possiblePaths.append(currentPath)
        return
    connectedNodes = caveMap[fromNode]
    for node in connectedNodes:
        if node != "start":
            if not node.islower() or node not in currentPath:
                getPaths(caveMap, node, currentPath,
                         possiblePaths, doubleVisitNode)
            elif node != "end" and not doubleVisitNode:
                getPaths(caveMap, node, currentPath, possiblePaths, node)


pattern = re.compile("^(\w+)-(\w+)$")
nodes = open("input.txt", "r").read().split("\n")
caveMap = {}
for node in nodes:
    matches = pattern.match(node)
    node = matches[1]
    connectedTo = matches[2]
    caveMap.setdefault(node, []).append(connectedTo)
    if connectedTo != "start" or connectedTo != "end":
        caveMap.setdefault(connectedTo, []).append(node)

paths = []
getPaths(caveMap, "start", [], paths)
print("Nr of paths:", len(paths))
