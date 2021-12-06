
def gamma(l, i):
    b = {'0': 0, '1': 0}
    for e in l:
        b[e[i]] += 1
    if b['0'] > b['1']:
        return 0
    else:
        return 1


def epsilon(l, i):
    b = {'0': 0, '1': 0}
    for e in l:
        b[e[i]] += 1
    if b['0'] > b['1']:
        return 1
    else:
        return 0


nums = []
with open("3Ainput.txt") as f:
    for line in f:
        nums.append(line.rstrip())

ogrcandidates = nums.copy()
for idx in range(len(nums[0])):
    g = gamma(ogrcandidates, idx)
    t = [e for e in ogrcandidates if int(e[idx]) == g]
    ogrcandidates = t
    if len(t) == 1:
        print(idx)
        break
print(ogrcandidates, int("".join(ogrcandidates), 2))

csrcandidates = nums.copy()
for idx in range(len(nums[0])):
    g = epsilon(csrcandidates, idx)
    t = [e for e in csrcandidates if int(e[idx]) == g]
    csrcandidates = t
    if len(t) == 1:
        print(idx)
        break
print(csrcandidates, int("".join(csrcandidates), 2))


print(int("".join(csrcandidates), 2) * int("".join(ogrcandidates), 2))
