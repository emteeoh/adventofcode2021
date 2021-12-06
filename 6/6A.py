
with open("6Ainput.txt") as file:
    fishes = [int(fish) for line in file for fish in line.split(",")]

print(len(fishes))

fishhist = {}
for i in fishes:
    try:
        fishhist[i] += 1
    except KeyError:
        fishhist[i] = 1

def nextday(fhist):
    fnd={}
    for k, v in fhist.items():
        if k == 0:
            try:
                fnd[6] = fnd[6] + v
            except KeyError:
                fnd[6] = v
            try:
                fnd[8] = fnd[8] + v
            except KeyError:
                fnd[8] = v
        else:
            try:
                fnd[k-1] = fnd[k-1] + v
            except KeyError:
                fnd[k-1] = v
    return fnd

for i in range(256):
    fnext = nextday(fishhist)
    print(", ".join(f"{k}:{v}" for k,v in sorted(fnext.items())))
    fishhist=fnext

print(sum([v for v in fishhist.values()]))



# def fishday(itr):
#     for i in itr:
#         if i == 0:
#             yield 6
#             yield 8
#         else:
#             yield i-1
#
#
# for i in range(80):
#     fishes = fishday(fishes)
#     print(80)
# for i in range(80):
#     fishes = fishday(fishes)
# print(160, len(list(fishes)))
# for i in range(80):
#     fishes = fishday(fishes)
# print(240, len(list(fishes)))
# for i in range(16):
#     fishes = fishday(fishes)
# print(256, len(list(fishes)))

