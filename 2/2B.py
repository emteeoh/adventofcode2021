
pos = 0
depth = 0
aim = 0
with open("2Ainput.txt") as f:
    for line in f:
        l = line.split(' ')
        if l[0] == 'forward':
            pos += int(l[1])
            depth += aim * int(l[1])
        elif l[0] == 'up':
            aim -= int(l[1])
        elif l[0] == 'down':
            aim += int(l[1])
        else:
            print("Bad line ", line )

print (pos*depth)

