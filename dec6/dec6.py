import threading
import math
import time
newFishLife = 8
respawnRate = 6
nrOfThreads = 8
days = 256

start = time.time()


def tickFish(fish: list, nrOfdays, result):
    print("Starting fish population:", fish)
    # lock = threading.Lock()
    for i in range(0, nrOfdays):
        nrOfFish = len(fish)
        print("Current nrOfFish:", nrOfFish)
        for j in range(0, nrOfFish):
            if fish[j] == 0:
                fish.append(newFishLife)
                fish[j] = respawnRate
            else:
                fish[j] -= 1
    # with lock:
    result.append(len(fish))
    print("Thread finished", len(fish))


input = open("input.txt", "r")
anglerFish = [int(x) for x in input.read().split(",")]
batchSize = math.ceil(len(anglerFish) / nrOfThreads)
batches = [anglerFish[i:i + batchSize]
           for i in range(0, len(anglerFish), batchSize)]
threads = []
result = []
print("Created batches:", batches)
for x in batches:
    thread = threading.Thread(target=tickFish, args=(x, days, result,))
    threads.append(thread)
    thread.start()

for t in threads:
    t.join()
print("Nr of fish:", sum(result))


# for i in range(0, days):
#     tickFish(anglerFish)
# print("Nr of fish:", len(anglerFish))
