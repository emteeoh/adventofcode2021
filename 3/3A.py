bits = {0: {}, 1: {}}
with open("3Ainput.txt") as f:
    for line in f:
        for i, b in enumerate(line):
            if b in ['0', '1']:
                try:
                    bits[int(b)][i] += 1
                except KeyError:
                    bits[int(b)][i] = 1


print(f"0: {[bits[0][k] for k in sorted(bits[0])]}")
print(f"1: {[bits[1][k] for k in sorted(bits[1])]}")
epsilon = 0
gamma = 0
elist = []
glist = []
for k in sorted(bits[0]):
    epsilon *= 2
    gamma *= 2
    if bits[0][k]>bits[1][k]:
        # Do nothing with gamma
        epsilon += 1
        glist.append(0)
        elist.append(1)
    else:
        gamma += 1
        # do nothing with epsilon
        glist.append(1)
        elist.append(0)

print(glist,elist)
print(gamma,epsilon)
print(gamma*epsilon)

