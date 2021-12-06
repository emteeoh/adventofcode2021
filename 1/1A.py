
with open("1Ainput.txt") as f:
    i = [ int(i) for i in f]
k = 0
for j in range(1,len(i)):
    id = (i[j]-i[j-1])>0
    if id:
        k += 1
print(k)
