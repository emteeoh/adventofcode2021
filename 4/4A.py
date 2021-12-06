boards = []
with open("4input.txt") as f:
    # first line is bingo numbers
    bingonums = [int(i) for i in f.readline().split(",")]
    f.readline()
    blines = [[int(i) for i in l.split()] for l in f]

tb = []
for line in blines:
    if line:
        tb.append(line)
    else:
        boards.append(tb)
        tb = []

# print(bingonums)
# print(boards)


def playbingo(board, nums):
    def scoreboard(bboard, board, lastnum):
        score = 0
        for i in range(5):
            for j in range(5):
                if not bboard[i][j]:
                    score += board[i][j]
        return score * lastnum

    def checkvert(bboard):
        for i in range(5):
            c=0
            for j in range(5):
                if bboard[j][i]:
                    c += 1
                else:
                    break
            if c == 5:
                return True
        return False

    def checkhoriz(bboard):
        for i in range(5):
            c=0
            for j in range(5):
                if bboard[i][j]:
                    c += 1
                else:
                    break
            if c == 5:
                return True
        return False


    # return score, cyclecount
    bboard = [[False for i in range(5)] for j in range(5)]
    for c,b in enumerate(nums):
        for i in range(5):
            for j in range(5):
                if board[i][j] == b:
                    bboard[i][j] = True
        if checkvert(bboard) or checkhoriz(bboard):
            return c, scoreboard(bboard,board,b)


bestr = len(bingonums) + 1
bests = 0
worstr = 0
worsts = 0
for b in boards:
    # print(b, bingonums, type(b), type(bingonums))
    r, s = playbingo(b, bingonums)
    if r < bestr:
        bestr = r
        bests = s
    if r > worstr:
        worstr = r
        worsts = s

print(bestr, bests)
print(worstr, worsts)
