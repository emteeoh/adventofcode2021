
with open("1Ainput.txt") as f:
    i = [int(i) for i in f]

j = [i[x]+i[x+1]+i[x+2] for x in range(len(i)-2)]

m = 0
for k in range(1,len(j)):
    if j[k]-j[k-1] > 0:
        m += 1

print(m)