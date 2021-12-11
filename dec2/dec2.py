file = open("input.txt", "r")
x = 0
y = 0
aim = 0
for line in file:
    input = line.split(" ")
    dir = input[0]
    value = int(input[1])
    if dir == "forward":
        x += value
        y += aim * value
    elif dir == "down":
        aim += value
    else:
        aim -= value
print("Final:", x * y)
