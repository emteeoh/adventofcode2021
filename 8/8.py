import collections

digit0 = frozenset('abcefg')
digit1 = frozenset('cf')
digit2 = frozenset('acdeg')
digit3 = frozenset('acdfg')
digit4 = frozenset('bcdf')
digit5 = frozenset('abdfg')
digit6 = frozenset('abdefg')
digit7 = frozenset('acf')
digit8 = frozenset('abcdefg')
digit9 = frozenset('abcdfg')
digits = {digit0: '0', digit1: '1', digit2: '2', digit3: '3', digit4: '4', digit5: '5', digit6: '6', digit7: '7', digit8: '8', digit9: '9'}
count = 0
with open("input.txt") as file:
    for line in file:
        # noinspection SpellCheckingInspection
        linesets = collections.defaultdict(list)
        linemap = {c: '' for c in digit8}
        segmenthist = {c: 0 for c in digit8}
        ii, oo = line.split("|")
        outputs = oo.strip().lstrip().split(" ")
        inputs = ii.strip().lstrip().split(" ")
        for d in inputs:
            # print(d,set(d))
            linesets[len(d)].append(set(d))
            for c in d:
                segmenthist[c] += 1
        print("linesets: ", linesets)
        print("segmenthist: ", segmenthist)
        # digit7 has segmentA as well as segmentC and segmentF. digit1 only has segmentC and segmentF
        linemap[set(linesets[3][0]).difference(linesets[2][0]).pop()] = 'a'
        print("linemap: ", linemap)
        # identify bcef based on histogram
        for k, v in segmenthist.items():
            if v == 4:
                linemap[k] = 'e'
            if v == 6:
                linemap[k] = 'b'
            if v == 8 and linemap[k] != 'a':
                linemap[k] = 'c'
            if v == 9:
                linemap[k] = 'f'
        print("linemap incomplete: ", linemap)
        # at this point we've unscrambled everything except segmentD and segmentG
        # the last unmapped segment in digit4 is segmentD
        for c in linesets[4][0]:
            if not linemap[c]:
                linemap[c] = 'd'
        # the one remaining unmapped segment is segmentG
        for c in digit8:
            if not linemap[c]:
                linemap[c] = 'g'
        print("linemap complete: ", linemap)
        correctedoutputs = []
        for n in outputs:  # n is a string
            s = ''
            for d in n:  # d is the segments in the digit represented by n
                s += linemap[d]  # linemap maps the scrambled segment to actual segment
            print(f"{n} -> {s} {frozenset(s)} {digits[frozenset(s)]}")
            correctedoutputs.append(digits[frozenset(s)])
        count += int("".join(correctedoutputs))
        print("correctedouputs: ", "".join(correctedoutputs), int("".join(correctedoutputs)))
    print(count)

