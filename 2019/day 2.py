#imagine spending 1 hour and 30 minutes trying to find .copy() HAHA fuck

original = [int(s) for s in input().split(',')]

g = 19690720

def parse(n, v, o):
    o = original.copy()
    o[1] = n
    o[2] = v
    c = 0

    while True:
        if o[c] == 1:
            o[o[c + 3]] = o[o[c + 1]] + o[o[c + 2]]
        elif o[c] == 2:
            o[o[c + 3]] = o[o[c + 1]] * o[o[c + 2]]
        elif o[c] == 99:
            if o[0] == g:
                return True
            else:
                #print(o[0], n, v)
                return False
        c += 4

for i in range(100):
    for j in range(100):
        if parse(i, j, original):
            print(100 * i + j)
            pass
        else:
            pass
