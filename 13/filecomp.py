
def comparefiles(i):
    mname = f"gridsave{i}.txt"
    tname = f"saves/savegrid{i}"

    mgrid = []
    with open(mname) as file:
        for line in file:
            mgrid.append(tuple(line.strip().split(',')))

    tgrid = []
    with open(tname) as file:
        for line in file:
            tgrid.append(tuple(line.strip().split(',')))

    tset = set(tgrid)
    mset = set(mgrid)

    if tset == mset:
        print(f"iteration {i} same!")
    else:
        print(f"iteration {i}: tgrid: {len(tset)}   mgrid: {len(mset)}")
        print(f"               in common: {len(mset.intersection(tset))}")
        print(f"               extras: {len(mset - tset)}")

        print(mset.intersection(tset))


comparefiles(2)