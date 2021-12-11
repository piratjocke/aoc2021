from collections import deque
fishRespawnRate = 9
spawnIndex = 8
newFishIndex = 6
days = 256
fishMap = deque([0] * fishRespawnRate)
fishes = [int(x) for x in open("input.txt", "r").read().split(",")]
# Populate map
for fish in fishes:
    fishMap[fish] += 1

for i in range(0, days):
    fishMap.rotate(-1)
    fishMap[newFishIndex] += fishMap[spawnIndex]

print("Nr of fish:", sum(fishMap))
