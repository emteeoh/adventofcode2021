from collections import Counter


infile = "input.txt"
pairRules = dict()
with open(infile) as file:
    polymerTemplate = file.readline().strip()
    file.readline()  # discard blank line
    for r in file:
        k,v = r.strip().split(" -> ")
        pairRules[k] = v

def lettercounter(pcount,last):
    lc = Counter()
    for p in pcount.keys():
        lc[p[0]] += pcount[p]
        lc[p[1]] += pcount[p]
    lc[last] += 1
    m = lc.most_common()
    print(f"lettercount")
    print(f"    input:{pcount}")
    print(f"    counts: {lc}")
    print(f"    max: {m[0][1]} min: {m[-1][1]}")
    print(f"    score: {m[0][1] - m[-1][1]}   half-score: {(m[0][1] - m[-1][1])//2}")


pairCount = Counter()
for i in range(len(polymerTemplate)-1):
    pairCount[polymerTemplate[i]+polymerTemplate[i+1]] += 1


rounds = 40
for _ in range(rounds):
    newPairCount = Counter()
    for pair in pairCount.keys():
        newPairCount[pair[0]+pairRules[pair]] += pairCount[pair]
        newPairCount[pairRules[pair]+pair[1]] += pairCount[pair]
    pairCount = newPairCount

lettercounter(pairCount,polymerTemplate[-1])



